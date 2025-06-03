
class Client:

    def __init__(self,id_cliente=None,nombre =None,apellido=None,id_membresia=None,fecha_registro=None,email=None):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido
        self._id_membresia=id_membresia
        self._fecha_registro = fecha_registro
        self._email = email

    def __str__(self):
        return f''' Cliente:
        id: {self._id_cliente}
        Nombre: {self._nombre}
        Apellido : {self._apellido}
        Membresia : {self._id_membresia}
        Fecha de registro : {self._fecha_registro}
        Email : {self._email}'''

    #Getters y setters
    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente (self,id_cliente):
        self._id_cliente = id_cliente


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def membresia(self):
        return self._id_membresia

    @membresia.setter
    def membresia(self,membresia):
        self._id_membresia = membresia


    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self,fecha_registro):
        self._fecha_registro = fecha_registro


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email = email

#pruebas locales

if __name__ == '__main__':

    #crear un objeto cliente
    cliente1 = Client(nombre='Camila',apellido='Sanchez',id_membresia=1,fecha_registro='2025-4-15',email='cam@email.com')
    print(cliente1.__str__())