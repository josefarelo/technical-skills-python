class Motor:
    def __init__(self, tipo="Gasolina"):
        self.tipo = tipo
        self.encendido = False
    
    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"Motor {self.tipo} arrancado")
        else:
            print("El motor ya estaba encendido")
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Motor apagado")
        else:
            print("El motor ya estaba apagado")

class Auto:
    def __init__(self, marca, modelo, motor=None):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor if motor else Motor()
    
    def encender(self):
        print(f"{self.marca} {self.modelo}: ", end="")
        self.motor.arrancar()
    
    def apagar(self):
        print(f"{self.marca} {self.modelo}: ", end="")
        self.motor.apagar()
    
    def cambiar_motor(self, nuevo_motor):
        self.motor = nuevo_motor
        print(f"Motor cambiado a {nuevo_motor.tipo}")

# Probando las clases
motor_electrico = Motor(tipo="Eléctrico")
mi_auto = Auto("Toyota", "Corolla")
mi_auto_electrico = Auto("Tesla", "Model S", motor_electrico)

print("--- Pruebas ---")
mi_auto.encender()
mi_auto.encender()  # Intentar encender ya encendido
mi_auto.apagar()

mi_auto_electrico.encender()
mi_auto_electrico.cambiar_motor(Motor(tipo="Híbrido"))
mi_auto_electrico.encender()