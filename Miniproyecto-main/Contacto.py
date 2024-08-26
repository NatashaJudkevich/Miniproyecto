class Contacto:

    def __init__(self, pnombre, ptelefono, pemail, pdireccion):
        self.nombre=pnombre
        self.telefono=ptelefono
        self.email=pemail
        self.direccion=pdireccion

    def __str__(self):
        return (f"Nombre:{self.nombre}\n Telefono:{self.telefono}\n Email:{self.email}\n Direccion:{self.direccion}\n")

    def actualizar(self, pnuevonombre=None, ptelefono=None, pemail=None, pdireccion=None):
        if pnuevonombre:
            self.nombre=pnuevonombre
        if ptelefono:
            self.telefono=ptelefono
        if pemail:
            self.email=pemail
        if pdireccion:
            self.pdireccion

        