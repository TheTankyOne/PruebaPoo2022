from re import X
from Cliente import Cliente

class Cuenta():
    def __init__(self, titular, saldo, movimientos):
        self.titular = titular
        self.saldo = float(saldo)
        self.movimientos = movimientos

    def get_titular(self):
        return self.get_titular
    def get_saldo(self):
        return self.saldo
    def get_movimientos(self):
        return self.get_movimientos 

    def set_titular(self, titular):
        self.titular =titular
    def set_saldo(self, saldo):
        self.saldo =saldo
    def set_movimientos(self, movimientos):
        self.movimientos =movimientos
    
    def deposito(self, saldo, x):
        print("ingrese el monto que quiera depositar: ")
        input (x)
        if x <= 0:
            print ("el monto no puede ser igual a 0")
            return
        else:
            print ("el nuevo monto es: " + (x+saldo)) 
            saldo = (x+saldo)
    
    def retiro(self, saldo, x):
        print("ingrese el monto que quiera retirar: ")
        input (x)
        if x <= 0 or x >= saldo:
            print ("el monto no puede ser igual a 0, o no puede ser mayor que el saldo acutal")
            return
        else:
            print ("el nuevo monto es: " + (saldo-x)) 
            saldo = (saldo-x)
    

    def  informacion_Cuenta(self, titular, saldo):
        return print("El nombre es " + titular + " y el saldo es " + saldo)

    def regristar_Movimiento(self):
        return None
