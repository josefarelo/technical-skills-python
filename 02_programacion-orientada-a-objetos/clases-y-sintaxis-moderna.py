class Persona:
    def __init__(self, nombre, edad, ciudad=None):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad if ciudad else "Desconocida"
    
    def __str__(self):
        if self.ciudad == "Desconocida":
            return f"{self.nombre} ({self.edad} años)"
        else:
            return f"{self.nombre} ({self.edad} años) - {self.ciudad}"
    
    def cumpleanios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años."

# Ejemplo de uso
persona1 = Persona("Lucía", 28)
print(persona1)  # Lucía (28 años)

persona2 = Persona("Carlos", 35, "Ciudad Autónoma de Buenos Aires")
print(persona2)  # Carlos (35 años) - Ciudad Autónoma de Buenos Aires

print(persona1.cumpleanios())  # ¡Feliz cumpleaños Lucía! Ahora tienes 29 años.
print(persona1)  # Lucía (29 años)