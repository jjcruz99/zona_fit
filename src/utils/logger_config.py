import logging as log

def setup_logging():
    log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers =[
                   log.FileHandler('capa_datos.log'),
                   log.StreamHandler()
                ])
    log.info('Logging configurado.')

#pruebas locales
if __name__ == '__main__':

    #llamar la funcion para configurar el lingging
    setup_logging()

    #mensajes de pruebas
    log.debug('Mensaje a nivel de debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel de critical')