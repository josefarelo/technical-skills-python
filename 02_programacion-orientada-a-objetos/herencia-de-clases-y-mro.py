class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} hace un sonido genérico")
    
    def moverse(self):
        print(f"{self.nombre} se mueve de alguna manera")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hablar(self):
        print(f"{self.nombre} el {self.raza} dice: ¡Guau!")
    
    def mover_cola(self):
        print(f"{self.nombre} mueve la cola feliz")

# Probando las clases
mi_animal = Animal("Bicho")
mi_animal.hablar()
mi_animal.moverse()

print("\n")

mi_perro = Perro("Firulais", "Labrador")
mi_perro.hablar()
mi_perro.moverse()
mi_perro.mover_cola()

# Mostrando información de herencia
print("\nInformación de herencia:")
print(f"¿Perro es subclase de Animal? {issubclass(Perro, Animal)}")
print(f"¿mi_perro es instancia de Perro? {isinstance(mi_perro, Perro)}")
print(f"¿mi_perro es instancia de Animal? {isinstance(mi_perro, Animal)}")