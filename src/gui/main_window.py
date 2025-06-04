import tkinter as tk
from tkinter import ttk,messagebox
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
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('1250x600')
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
        print('hola desde mostrar formulario')
        self.frame_formulario = ttk.Frame(self)

        label_nombre = ttk.Label(self.frame_formulario,text='Nombre')
        label_nombre.grid(row=0,column=0,sticky=tk.W,pady=10,padx=5)
        self.entrada_nombre = ttk.Entry(self.frame_formulario,width=40)
        self.entrada_nombre.grid(row=0,column=1)

        label_apellido = ttk.Label(self.frame_formulario,text='Apellido')
        label_apellido.grid(row=1,column=0,sticky=tk.W,pady=10,padx=5)
        self.entrada_apellido = ttk.Entry(self.frame_formulario,width=40)
        self.entrada_apellido.grid(row=1,column=1)

        label_membresia = ttk.Label(self.frame_formulario,text='Membresia')
        label_membresia.grid(row=2,column=0,sticky=tk.W,pady=10,padx=5)
        self.entrada_membresia = ttk.Entry(self.frame_formulario,width=40)
        self.entrada_membresia.grid(row=2,column=1)

        label_fecha_registro = ttk.Label(self.frame_formulario,text='Fecha de registro')
        label_fecha_registro.grid(row=3,column=0,sticky=tk.W,pady=10,padx=5)
        self.entrada_fecha_registro = ttk.Entry(self.frame_formulario,width=40)
        self.entrada_fecha_registro.grid(row=3,column=1)

        label_email = ttk.Label(self.frame_formulario,text='Email')
        label_email.grid(row=4,column=0,sticky=tk.W,pady=10,padx=5)
        self.entrada_email = ttk.Entry(self.frame_formulario,width=40)
        self.entrada_email.grid(row=4,column=1)

        #publicar frame
        self.frame_formulario.grid(row=1, column=0)

        #estilos para el formulario
        # Estilo para Labels
        self.estilos.configure('TLabel',
                               font=('Arial', 12, 'bold'),
                               foreground='white',
                               padding=5)

        # Estilo para Entrys
        self.estilos.configure('TEntry',padding=5,
                               font=('Arial', 12),
                               foreground='black',
                               fieldbackground='white',
                               bordercolor='gray',
                               borderwidth=1,
                               relief='solid')


    def mostrar_tabla(self):
        #crear tabla
        self.frame_tabla = ttk.Frame(self)

        #estilos para la tabla
        self.estilos.configure('Treeview',background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20,
                               font=('Arial',12))
        # Estilo para las cabeceras de la tabla
        self.estilos.configure('Treeview.Heading',
                               font=('Arial', 12, 'bold'))


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
        self.tabla.column(columnas[1],anchor=tk.CENTER, width=120)
        self.tabla.column(columnas[2],anchor=tk.CENTER, width=120)
        self.tabla.column(columnas[3],anchor=tk.CENTER, width=100)
        self.tabla.column(columnas[4],anchor=tk.CENTER, width=150)
        self.tabla.column(columnas[5],anchor=tk.CENTER, width=240)

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

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.grid(row=2,column=0,columnspan=2)

        #Crear botones
        boton_agregar = ttk.Button(self.frame_botones,text='Guardar',
                                   command=self.guardar_cliente)
        boton_agregar.grid(row=0,column=0,padx=20,pady=50)

        boton_eliminar = ttk.Button(self.frame_botones,text='Eliminar',
                                   command=self.eliminar_cliente)
        boton_eliminar.grid(row=0,column=1,padx=20,pady=50)

        boton_actualizar = ttk.Button(self.frame_botones,text='Actualizar',
                                   command=self.actualizar_cliente)
        boton_actualizar.grid(row=0,column=2,padx=20,pady=50)

        boton_limpiar = ttk.Button(self.frame_botones,text='Limpiar',
                                   command=self.limpiar_datos)
        boton_limpiar.grid(row=0,column=3,padx=20,pady=40)

        #Estilos botones
        self.estilos.configure('TButton',background='#005f73',font=12,padding=10,relief='ridge')
        self.estilos.map('TButton',background=[('active','#0a9396')])

    def guardar_cliente(self):
        pass

    def eliminar_cliente(self):
        pass

    def actualizar_cliente(self):
        pass

    def limpiar_datos(self):
        pass

if __name__ == '__main__':
    from src.utils.logger_config import setup_logging
    setup_logging()

    ventana1= MainWindow()
    ventana1.mainloop()

