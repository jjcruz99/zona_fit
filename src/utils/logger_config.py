import logging as log
import os

def setup_logging():
    log_file_path = os.path.join(os.path.dirname(__file__), 'capa_de_datos.log')
    log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers =[
                   log.FileHandler(log_file_path,encoding='UTF8'),
                   log.StreamHandler()
                ])
    log.info('Logging configurado.')

#pruebas locales
if __name__ == '__main__':

    #llamar la funcion para configurar el longging
    setup_logging()

    #mensajes de pruebas
    log.debug('Mensaje a nivel de debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel de critical')