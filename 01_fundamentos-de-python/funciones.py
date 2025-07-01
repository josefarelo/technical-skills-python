# Función para saludar a una persona
def saludar(nombre):
    saludo = f"Hola, {nombre}!"
    return saludo

# Función lambda para calcular el cuadrado de un número
cuadrado = lambda numero: numero * numero

# Ejemplos de uso
nombre_persona = "María"
print(saludar(nombre_persona))

numero_a_elevar = 5
resultado = cuadrado(numero_a_elevar)
print(f"El cuadrado de {numero_a_elevar} es {resultado}")

# Probando con otros valores
print(saludar("Carlos"))
print(f"3 al cuadrado es: {cuadrado(3)}")