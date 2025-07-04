class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # Atributo privado
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: ${cantidad}")
        else:
            print("Error: La cantidad debe ser positiva")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado: ${cantidad}")
        else:
            print("Error: Fondos insuficientes o cantidad inválida")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.__saldo}")

# Ejemplo de uso
mi_cuenta = CuentaBancaria(1000)
mi_cuenta.mostrar_saldo()
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(2000)  # Esto mostrará error
mi_cuenta.mostrar_saldo()