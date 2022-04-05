from datetime import date


class Persona():
    def __init__(self, nombre, fecha_nacimiento, rut):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
    

    def get_nombre(self):
        return self.nombre

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_rut(self):
        return self.rut

    def set_nombre(self, nombre):
        self.nombre =nombre

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento =fecha_nacimiento

    def set_rut(self, rut):
        self.rut =rut

    
    def  informacion_persona(self, nombre, fecha_nacimiento, rut):
        return print("El nombre es " + nombre + " la fecha de nacimiento es " + fecha_nacimiento + " y el rut es " + rut)
    
    def digito_verificador(rut):
        value = 11 - sum([ int(a)*int(b)  for a,b in zip(str(rut).zfill(8), '32765432')])%11
        return {10: 'K', 11: '0'}.get(value, str(value))

    def Edad(fecha_nacimiento):
        today = date.today()
        Edad = today.year - fecha_nacimiento,.year - ((today.month, today.day) < (fecha_nacimiento,.month, fecha_nacimiento,.day))
        return Edad

    
    def calcular_Edad(self, Edad):
        if Edad >= 18:
            print ("Es mayor de edad")
        else:
            print ("es menor de edad")
            
