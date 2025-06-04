import tkinter as tk
from tkinter import ttk
from src.services.client_service import ClientService


class MainWindow(tk.Tk):

    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()
        #metodos para configurar ventana
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('1100x600')
        self.title('Zona Fit App')
        self.configure(background=MainWindow.COLOR_VENTANA)

        #Estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self,background = MainWindow.COLOR_VENTANA,
                               foreground='white',
                               filedbackground='black')

    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)

    def mostrar_titulo(self):
        etiqueta_titulo = ttk.Label(self,text='Zona Fit GYM',
                                    font=('Arial',20),
                                    background=MainWindow.COLOR_VENTANA,
                                    foreground='white')
        etiqueta_titulo.grid(row=0,column=0,columnspan=2,pady=20)

    def mostrar_formulario(self):
        pass

    def mostrar_tabla(self):
        #crear tabla
        self.frame_tabla = ttk.Frame(self)
        self.estilos.configure('Treeview',background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)
        #Columnas de la tabla
        columnas = ('Id','Nombre','Apellido','Membresia','Fecha de registro', 'Email')
        self.tabla = ttk.Treeview(self.frame_tabla,columns=columnas,show='headings')
        self.tabla.grid(row=0,column=0)
        self.frame_tabla.grid(row=1,column=1,padx=20)

        #cabeceros de la tabla
        self.tabla.heading(columnas[0],text=columnas[0], anchor=tk.CENTER)
        self.tabla.heading(columnas[1],text=columnas[1], anchor=tk.W)
        self.tabla.heading(columnas[2],text=columnas[2], anchor=tk.W)
        self.tabla.heading(columnas[3],text=columnas[3], anchor=tk.W)
        self.tabla.heading(columnas[4],text=columnas[4], anchor=tk.W)
        self.tabla.heading(columnas[5],text=columnas[5], anchor=tk.W)

        #Definir las columnas
        self.tabla.column(columnas[0],anchor=tk.CENTER, width=50)
        self.tabla.column(columnas[1],anchor=tk.CENTER, width=100)
        self.tabla.column(columnas[2],anchor=tk.CENTER, width=100)
        self.tabla.column(columnas[3],anchor=tk.CENTER, width=100)
        self.tabla.column(columnas[4],anchor=tk.CENTER, width=100)
        self.tabla.column(columnas[5],anchor=tk.CENTER, width=150)

        #Cargar los datos de los clientes
        clientes = ClientService.obtener_todos_clientes()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id_cliente,
                                      cliente.nombre,
                                      cliente.apellido,
                                      cliente.membresia,
                                      cliente.fecha_registro,
                                      cliente.email))

        #scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1, sticky=tk.NS)


if __name__ == '__main__':
    from src.utils.logger_config import setup_logging
    setup_logging()

    ventana1= MainWindow()
    ventana1.mainloop()

