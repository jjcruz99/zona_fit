
from src.database.client_dao import ClientDAO
from src.utils.logger_config import log
from src.models.client import Client

class ClientService:

    @staticmethod
    def obtener_todos_clientes ():
        try:
            lista_clientes = ClientDAO.obtener_clientes()
            return lista_clientes
        except Exception as e:
            log.error(f'Ocurrio un error al obtener clientes. Detalles:{e}')
            return []

    @staticmethod
    def registrar_nuevo_cliente(nuevo_cliente):
        try:
            id_generado = ClientDAO.insertar_cliente(nuevo_cliente)
            if id_generado:
                print(f'Se insertó un nuevo cliente con el ID: {id_generado}')
                return id_generado
            else:
                print('No se pudo insertar el cliente.')
                return id_generado
        except Exception as e:
            log.error(f'Ocurrio un error al intentar insertar cliente. Detalles:{e}')


    @staticmethod
    def actualizar_datos_cliente(cliente_actualizar):
        try:
            respuesta = ClientDAO.actualizar_cliente(cliente_actualizar)
            if respuesta:
                print(f'Se actualizo  cliente con el ID: {cliente_actualizar.id_cliente}')
                return respuesta
            else:
                print('No se pudo actualizar el cliente.')
                return respuesta
        except Exception as e:
            log.error(f'Ocurrio un error al actulizar datos del cliente. Detalles:{e}')


    @staticmethod
    def eliminar_cliente(id_cliente_eliminar):
        try:
            respuesta = ClientDAO.eliminar_cliente(id_cliente_eliminar)
            if respuesta:
                print(f'Se elimino cliente con el ID: {id_cliente_eliminar}')
                return respuesta
            else:
                print('No se pudo eliminar el cliente.')
                return respuesta
        except Exception as e:
            log.error(f'Ocurrio un error al intentar insertar cliente. Detalles:{e}')


    @staticmethod
    def validar_formulario_cliente(datos_cliente):
        if datos_cliente.nombre and datos_cliente.apellido and datos_cliente.membresia and datos_cliente.fecha_registro and datos_cliente.email:
            return True
        else:
            return False


#pruebas
if __name__ == '__main__':

    from src.utils.logger_config import setup_logging
    setup_logging()

    #probar el metodo obtener clientes
    lista_clientes = ClientService.obtener_todos_clientes()
    for cliente in  lista_clientes:
        print(cliente.__str__())

    #probar metodo para insertar valores
    # cliente_prueba = Client(nombre='Luisa', apellido='Martinez', id_membresia=1, email='luisa.m@correo.com')
    # id_generado = ClientService.registrar_nuevo_cliente(cliente_prueba)

    # #probar metodo para actualizar valores
    # cliente_prueba = Client(id_cliente=3,nombre='Luisa', apellido='Martinez', id_membresia=1, fecha_registro='2025-05-30', email='luisa.m@correo.com')
    # respuesta = ClientService.actualizar_datos_cliente(cliente_prueba)


    #Probar metodo para eliminar cliente
    # id_cliente_eliminado='3'
    # respuesta = ClientService.eliminar_cliente(id_cliente_eliminado)
