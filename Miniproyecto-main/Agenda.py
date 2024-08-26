from Contacto import Contacto

class Agenda:

    def __init__(self):
        self.listacontactos= []

    def buscar_contacto(self,nombre):
        for contacto in self.listacontactos:
            if contacto.nombre == nombre:
                print(contacto)
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
            contacto.actualizar(nuevonombre, telefono, direccion, email)
        else:
            print("no existe")

    def listar_contactos(self):
        for contacto in self.listacontactos:
            print(contacto)

contacto1 = Contacto("Juan Pérez", "123456789", "juan@example.com", "Calle Falsa 123")
contacto2 = Contacto("Ana Gomez", "987654321", "ana@example.com", "Avenida Siempreviva 456")

agendita=Agenda()
agendita.agregar_contacto(contacto1)
agendita.agregar_contacto(contacto2)

#agendita.listar_contactos()

#agendita.editar_contacto("Juan Pérez", nuevonombre="Pepito", telefono="1122334455")
#agendita.listar_contactos()

#agendita.eliminar_contacto("Pepito")
#agendita.listar_contactos()

agendita.buscar_contacto("Ana Gomez")

agendita.listar_contactos()