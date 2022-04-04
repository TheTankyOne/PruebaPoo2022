from Cliente import Cliente

class Cuenta():
    def __init__(self, titular, saldo, movimientos):
        super.__init__(titular)
        self.saldo = float(saldo)
        self.movimientos = float(movimientos)


    def get_saldo(self):
        return self.saldo


    def set_saldo(self, saldo):
        self.saldo =saldo

    