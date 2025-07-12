class Caja:
    def __init__(self, valor):
        self.valor = valor
    
    def map(self, funcion):
        try:
            resultado = funcion(self.valor)
            return Caja(resultado)
        except Exception as e:
            print(f"Error al mapear: {e}")
            return self
    
    def __str__(self):
        return f"Caja({self.valor})"
    
    def __repr__(self):
        return self.__str__()

# Ejemplos
if __name__ == "__main__":
    # Caso básico
    caja_numero = Caja(5)
    caja_doble = caja_numero.map(lambda x: x * 2)
    print(caja_doble)  # Caja(10)
    
    # Cadena de mapeos
    caja_final = (
        Caja(3)
        .map(lambda x: x + 2)
        .map(lambda x: x ** 2)
        .map(str)
    )
    print(caja_final)  # Caja(25)
    
    # Mapeo con error
    caja_error = Caja("hola").map(lambda x: x.upper())
    print(caja_error)  # Caja(HOLA)
    
    caja_mal = Caja("texto").map(lambda x: x + 5)  # Error, pero no se rompe
    print(caja_mal)  # Mantiene el valor original