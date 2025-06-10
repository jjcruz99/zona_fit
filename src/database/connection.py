from src.utils.logger_config import log
from psycopg2 import pool
from src.config.settings import DB_CONFIG,POOL_CONFIG

class Connection:
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(POOL_CONFIG['min_con'],
                                                      POOL_CONFIG['max_con'],
                                                      host=DB_CONFIG['host'],
                                                      user=DB_CONFIG['username'],
                                                      password=DB_CONFIG['password'],
                                                      port=DB_CONFIG['db_port'],
                                                      database=DB_CONFIG['database'])
                log.debug(f'Creacion del pool EXITOSA: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrió un error al crear el pool de conexiones: {e}")
                raise  #permite que la capa superior maneje el error
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        ##Obtener objeto de conexiones
        conexion = cls.obtener_pool().getconn()
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresa la conexión al pool : {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
        log.debug('Se cerraron todas las conexiones')

#Pruebas locales
if __name__ == '__main__':
    from src.utils.logger_config import setup_logging
    setup_logging()
    conexion1 = Connection.obtener_conexion()
    Connection.liberar_conexion(conexion1)

    conexion2 = Connection.obtener_conexion()
    Connection.liberar_conexion(conexion2)

    #cerrar todas las conexiones
    Connection.cerrar_conexiones()