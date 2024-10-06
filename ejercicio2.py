class CuentaBancaria:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = saldo
        
    
    def depositar(self,ingreso):
        if self.saldo >= 0:
            self.saldo += ingreso
            print(f"se han depositado {ingreso}$")
        else:
            print("la cantidad ingresada debe ser positiva")
    def retirar(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print(f"saldo insuficiente")
    def Estado(self):
        print(f"El estdo actual de su cuenta es de {self.saldo}$")


cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.Estado()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(1500)