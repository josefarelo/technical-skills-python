from functools import reduce

# Lista de números para trabajar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando map para calcular cuadrados
def calcular_cuadrado(num):
    return num ** 2

cuadrados = list(map(calcular_cuadrado, numeros))

# Usando filter para números pares
def es_par(num):
    return num % 2 == 0

pares = list(filter(es_par, numeros))

# Usando reduce para sumar todos los números
def sumar(a, b):
    return a + b

suma_total = reduce(sumar, numeros)

# filter + map para cuadrados de números impares
def es_impar(num):
    return not es_par(num)

cuadrados_impares = list(map(calcular_cuadrado, filter(es_impar, numeros)))

# Mostrar resultados
print("Lista original:", numeros)
print("Cuadrados de todos:", cuadrados)
print("Números pares:", pares)
print("Suma total:", suma_total)
print("Cuadrados de impares:", cuadrados_impares)

# Ejemplo adicional con strings
palabras = ["hola", "mundo", "python", "programación"]

# Longitud de cada palabra
longitudes = list(map(len, palabras))
print("\nLongitudes de palabras:", longitudes)

# Filtrar palabras con más de 5 letras
largas = list(filter(lambda p: len(p) > 5, palabras))
print("Palabras largas:", largas)