from Persona import Persona

class Cliente():
    def __init__(self, nombre, fecha_nacimiento, rut):
        super().__init__(nombre, fecha_nacimiento, rut)
    

    def  password(self):
        self.password = [10]

    def productos_bancarios(self, productos_bancarios):
        self.productos_bancarios = productos_bancarios