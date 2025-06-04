
from src.models.client import Client
from src.utils.logger_config import log
from src.database.cursor_from_pool import CursorFromPool

class ClientDAO:

    #atributos de clase
    _SELECT_ALL = 'SELECT * FROM cliente'
    _INSERT = 'INSERT INTO cliente(nombre, apellido, id_membresia, email) VALUES(%s, %s, %s, %s) RETURNING id_cliente'
    _UPDATE = 'UPDATE cliente SET nombre=%s,apellido=%s,id_membresia=%s,fecha_registro=%s,email=%s WHERE id_cliente=%s'
    _DELETE = 'DELETE FROM cliente WHERE id_cliente=%s'

    #metodos de clase para realizar operaciones CRUD
    @classmethod
    def obtener_clientes(cls):
        try:
            with CursorFromPool() as cursor:
                cursor.execute(cls._SELECT_ALL)
                registros = cursor.fetchall()
                lista_clientes = []
                for registro in registros:
                    cliente = Client(id_cliente=registro[0], nombre=registro[1], apellido=registro[2],
                              id_membresia=registro[3], fecha_registro=registro[4], email=registro[5])
                    lista_clientes.append(cliente)
                return lista_clientes
        except Exception as e:
            log.error(f'Error al obtener los clientes. Detalles: {e}')
            return []

    @classmethod
    def insertar_cliente(cls,cliente):
        try:
            with CursorFromPool() as cursor:
                #tupla para insertar los datos
                datos_cliente = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.email)
                cursor.execute(cls._INSERT,datos_cliente)
                #obtener el id del cliente insertado
                id_cliente_nuevo = cursor.fetchone()[0]
                log.debug('Cliente insertado con EXITO')
                return id_cliente_nuevo
        except Exception as e:
            log.error(f'Error al insertar el cliente. Detalles : {e}')
            return 0

    @classmethod
    def actualizar_cliente(cls,cliente):
        try:
            with CursorFromPool() as cursor:
                datos_cliente = (cliente.nombre, cliente.apellido, cliente.membresia,cliente.fecha_registro, cliente.email,cliente.id_cliente)
                cursor.execute(cls._UPDATE,datos_cliente)
                log.debug(f'Se actualizaron los datos del cliente con id: {cliente.id_cliente}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Error al actualizar cliente. Detalles : {e}')
            return 0

    @classmethod
    def eliminar_cliente(cls,id):
        try:
            with CursorFromPool() as cursor:
                cursor.execute(cls._DELETE,(id,))
                log.debug(f'Se elimino el cliente con id: {id}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Error al eliminar cliente. Detalles : {e}')
            return 0


#pruebas
if __name__ == '__main__':

    from src.utils.logger_config import setup_logging
    setup_logging()

    #probar el metodo obtener clientes
    lista_clientes = ClientDAO.obtener_clientes()
    for cliente in  lista_clientes:
        print(cliente.__str__())

    #probar metodo para insertar valores
    # cliente_prueba = Client(nombre='Luisa', apellido='Martinez', id_membresia=1, email='luisa.m@correo.com')
    # id_generado = ClientDAO.insertar_cliente(cliente_prueba)
    # if id_generado:
    #     log.info(f'Se insertó un nuevo cliente con el ID: {id_generado}')
    # else:
    #     log.error('No se pudo insertar el cliente.')

    # #probar metodo para actualizar valores
    # cliente_prueba = Client(id_cliente=2,nombre='Luisa', apellido='Martinez', id_membresia=1, fecha_registro='2025-05-30', email='luisa.m@correo.com')
    # respuesta = ClientDAO.actualizar_cliente(cliente_prueba)
    # if respuesta:
    #     log.info(f'Se actualizo  cliente con el ID: {cliente_prueba.id_cliente}')
    # else:
    #     log.error('No se pudo actualizar el cliente.')

    #Probar metodo para eliminar cliente
    # id_cliente_eliminado='2'
    # respuesta = ClientDAO.eliminar_cliente(id_cliente_eliminado)
    # if respuesta:
    #     log.info(f'Se elimino cliente con el ID: {id_cliente_eliminado}')
    # else:
    #     log.error('No se pudo eliminar el cliente.')