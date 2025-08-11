class SumaStrategy:
    def calcular(self, num1, num2):
        resultado = num1 + num2
        print(f"Suma: {num1} + {num2} = {resultado}")
        return resultado

class MultiplicacionStrategy:
    def calcular(self, num1, num2):
        resultado = num1 * num2
        print(f"Multiplicación: {num1} * {num2} = {resultado}")
        return resultado

class DivisionStrategy:
    def calcular(self, num1, num2):
        if num2 == 0:
            raise ValueError("No se puede dividir por cero!")
        resultado = num1 / num2
        print(f"División: {num1} / {num2} = {resultado}")
        return resultado

class Calculadora:
    def __init__(self):
        self.estrategia = None

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia
        print(f"Estrategia cambiada a: {type(estrategia).__name__}")

    def calcular(self, a, b):
        if self.estrategia is None:
            raise ValueError("No se ha establecido una estrategia!")
        return self.estrategia.calcular(a, b)

# Ejemplo
if __name__ == "__main__":
    calc = Calculadora()

    # Usar suma
    calc.set_estrategia(SumaStrategy())
    calc.calcular(5, 3)

    # Cambiar a multiplicación
    calc.set_estrategia(MultiplicacionStrategy())
    calc.calcular(5, 3)

    # Cambiar a división
    calc.set_estrategia(DivisionStrategy())
    calc.calcular(10, 2)

    # Probar división por cero (manejo de error)
    try:
        calc.calcular(5, 0)
    except ValueError as e:
        print(f"Error: {e}")