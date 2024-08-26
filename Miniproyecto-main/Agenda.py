from Contacto import Contacto

class Agenda:

    def __init__(self):
        self.listacontactos= []

    def buscar_contacto(self,nombre):
        for contacto in self.listacontactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def agregar_contacto(self, contacto):
        self.listacontactos.append(contacto)

    def eliminar_contacto(self,nombre):
        contacto= self.buscar_contacto(nombre)
        if contacto:
            self.listacontactos.remove(contacto)

    def editar_contacto(self,nombre, nuevonombre=None,telefono=None,direccion=None,email=None):
        contacto =self.buscar_contacto(nombre)
        if contacto:
            contacto.actualizar(nuevonombre, telefono, direccion, email )
        else:
            print("no existe")

    def listar_contactos(self):
        for contacto in self.contactos:
            print("Listado de Contactos")
            print(contacto)
    
agendita=Agenda()
agendita.eliminar_contacto

