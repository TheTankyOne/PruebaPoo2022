from Persona import Persona

class Ejecutivo():
    def __init__(self, nombre, fecha_nacimiento, rut):
        super().__init__(nombre, fecha_nacimiento, rut)
    
    def  password(self):
        self.password = [10]
    def  usuario(self):
        self.usuario = [10]