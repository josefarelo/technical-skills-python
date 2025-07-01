class Persona:
    def __init__(self, nombre, edad=0):
        self.nombre = nombre
        self.edad = edad
        self.vivo = True
    
    def saludar(self):
        print(f"¡Hola! Me llamo {self.nombre}.")
        if self.edad > 0:
            print(f"Tengo {self.edad} años.")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Ahora tengo {self.edad} años!")
    
    def morir(self):
        self.vivo = False
        print(f"{self.nombre} ha muerto :(")

# Crear personas
persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos")

# Interactuar con los objetos
persona1.saludar()
persona2.saludar()

persona1.cumplir_anios()
persona2.cumplir_anios()

persona2.edad = 10  # Modificar atributo directamente
print(f"{persona2.nombre} ahora tiene {persona2.edad}")

persona1.morir()
print(f"¿{persona1.nombre} está viva? {persona1.vivo}")