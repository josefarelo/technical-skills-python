def calcular_suma(numero_1: int, numero_2: int) -> int:
    #Sumar dos números enteros y devuolver el resultado.
    resultado = numero_1 + numero_2
    return resultado

def main():
    # Ejemplo
    a = 5
    b = 3
    suma = calcular_suma(a, b)
    print(f"La suma de {a} y {b} es: {suma}")

if __name__ == "__main__":
    main()