from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def calcular_area_total(figuras):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total

# Ejemplo
if __name__ == "__main__":
    mis_figuras = [
        Rectangulo(5, 3),
        Circulo(2),
        Triangulo(4, 6),
        Cuadrado(5)
    ]
    
    resultado = calcular_area_total(mis_figuras)
    print(f"El área total de todas las figuras es: {resultado:.2f}")
    
    # Mostrar áreas individuales
    for i, figura in enumerate(mis_figuras, 1):
        print(f"Figura {i}: {figura.area():.2f}")