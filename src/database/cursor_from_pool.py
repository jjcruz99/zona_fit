from connection import Connection
from src.utils.logger_config import log

class CursorFromPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Connection.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb): #exc_tb = detalle de la Exepcion
        log.debug('Se ejecuta metodo __exit__')
        #Se verifica si ha ocurrido una exepcion
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrio una exepcion, se hace rollback : {exc_val} {exc_type} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug(('Commit de la transacción'))
        self._cursor.close()
        Connection.liberar_conexion(self._conexion)

#pruebas locales
if __name__ == '__main__':

    from src.utils.logger_config import setup_logging

    setup_logging()  # Lo llamar la configuracion para la prueba
    try:
        ## se llama indirectamente __init__ y __enter__ y cuando termina el with se llama __exit__
        with CursorFromPool() as cursor:
            cursor.execute('SELECT * FROM cliente')
            print('Listado de clientes:')
            print(cursor.fetchall())
    except Exception as e:
        log.error(f"Error al probar el cursor: {e}")

