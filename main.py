
from src.gui.login import Login
from src.gui.main_window import MainWindow
from src.utils.logger_config import setup_logging,log

if __name__ == '__main__':
    setup_logging()

    ventana_login = Login()
    ventana_login.mainloop()

    if ventana_login.login_exitoso:
        ventana_principal = MainWindow()
        ventana_principal.mainloop()
    else:
        log.info("Inicio de sesión cancelado. El programa ha finalizado.")