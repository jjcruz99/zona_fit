import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.config.settings import ADMIN

class Login(tk.Tk):

    def __init__(self):
        super().__init__()
        self._login_exitoso = False
        self.geometry('600x400+500+200')
        self.title("Login")
        self.configure(background='#1d2d44')
        # grid de la ventana
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self._crear_componentes()

    @property
    def login_exitoso(self):
        return self._login_exitoso

    @login_exitoso.setter
    def login_exitoso(self):
        self._login_exitoso = True


    def _crear_componentes(self):
        #agregar frame
        frame = ttk.Frame(self)
        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=3)

        #titulo
        etiqueta = ttk.Label(frame, text='Login', font=('Arial',26,'bold'))
        etiqueta.grid(row=0,column=0,columnspan=2,pady=20)

        #usuario
        etiqueta_usuario = ttk.Label(frame, text='Usuario', font=('Arial',16))
        etiqueta_usuario.grid(row=1,column=0,sticky=tk.W,padx=5,pady=10)

        self.usuario_caja_texto = ttk.Entry(frame,font=('Arial',16))
        self.usuario_caja_texto.grid(row=1,column=1,sticky=tk.W,padx=10,pady=10)

        #clave
        etiqueta_clave = ttk.Label(frame, text='Password', font=('Arial',16))
        etiqueta_clave.grid(row=2,column=0,sticky=tk.W,padx=10,pady=10)

        self.clave_caja_texto = ttk.Entry(frame,show='*',font=('Arial',16))
        self.clave_caja_texto.grid(row=2,column=1,sticky=tk.W,padx=5,pady=10)

        #boton
        login_boton = ttk.Button(frame, text='Enviar')
        login_boton.grid(row=3,column=0,columnspan=2,padx=5,pady=40)

        #eventos del boton
        login_boton.bind('<Return>',self.validar) #llama al evento validar al presionar enter
        login_boton.bind('<Button-1>',self.validar) #llama al evento validar al presionar click izq
        #Estilos
        estilos = ttk.Style()
        estilos.theme_use('clam')
        estilos.configure(self,background='#1d2d44',foreground='white',fieldbackground='black')
        estilos.configure('TButton',background='#005f73',font=('Arial',16,'bold'),padding=10,relief='raised',borderwidth=5)
        estilos.map('TButton',background=[('active','#0A9396')])
        # publicar
        frame.grid(column=0,row=0)

    #metdodo para validar admin
    def validar(self,event):
        usuario = self.usuario_caja_texto.get()
        clave = self.clave_caja_texto.get()
        if usuario == ADMIN['usuario'] and clave == ADMIN['clave']:
            messagebox.showinfo(title='Login', message='Datos correctos')
            self._login_exitoso = True
            self.after(50,self.destroy)
        else:
            messagebox.showerror(title='Login', message='Datos incorrectos')
            self.clave_caja_texto.delete(0,'end')


