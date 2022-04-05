from Cuenta import Cuenta

class Cuenta_Joven():
    def __init__(self, titular, saldo, movimientos, Bonificacion):
        super.__init__( titular, saldo, movimientos)
        self.Bonificacion = Bonificacion
    def get_Bonificacion(self):
        return self.get_Bonificacion
    def set_Bonificacion(self, Bonificacion):
        self.Bonificacion =Bonificacion