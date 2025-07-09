def aplicar_funcion(lista, funcion):
    resultado = []
    for elemento in lista:
        try:
            resultado.append(funcion(elemento))
        except Exception as e:
            print(f"Error al aplicar la función a {elemento}: {e}")
            resultado.append(None)
    return resultado

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Elevar al cuadrado
    numeros = [1, 2, 3, 4, 5]
    cuadrados = aplicar_funcion(numeros, lambda x: x ** 2)
    print("Cuadrados:", cuadrados)  # [1, 4, 9, 16, 25]
    
    # Ejemplo 2: Convertir a string
    mezcla = [1, "hola", 3.14, True]
    strings = aplicar_funcion(mezcla, str)
    print("Strings:", strings)  # ['1', 'hola', '3.14', 'True']
    
    # Ejemplo 3: Función que puede fallar
    def inverso(x):
        return 1 / x
    
    divisores = [1, 2, 0, 4]
    resultados = aplicar_funcion(divisores, inverso)
    print("Inversos:", resultados)  # [1.0, 0.5, None, 0.25]