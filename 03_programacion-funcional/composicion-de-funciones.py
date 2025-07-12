def multiplicar_por_dos(numero):
    resultado = numero * 2
    return resultado

def sumar_tres(numero):
    resultado = numero + 3
    return resultado

def componer_funciones(funcion1, funcion2):
    def funcion_compuesta(x):
        return funcion1(funcion2(x))
    return funcion_compuesta

# Probamos las funciones básicas
print("5 * 2 =", multiplicar_por_dos(5))  # Debería dar 10
print("5 + 3 =", sumar_tres(5))          # Debería dar 8

# Creamos función compuesta (primero suma 3, luego multiplica por 2)
funcion_compuesta = componer_funciones(multiplicar_por_dos, sumar_tres)

# Probamos con diferentes valores
valor_prueba = 4
resultado = funcion_compuesta(valor_prueba)
print(f"f(g({valor_prueba})) = (4 + 3) * 2 = {resultado}")  # Debería dar 14

valor_prueba = 10
resultado = funcion_compuesta(valor_prueba)
print(f"f(g({valor_prueba})) = (10 + 3) * 2 = {resultado}")  # Debería dar 26

# Extra: probamos al revés (multiplicar primero, luego sumar)
funcion_compuesta_reversa = componer_funciones(sumar_tres, multiplicar_por_dos)
valor_prueba = 5
resultado = funcion_compuesta_reversa(valor_prueba)
print(f"f(g({valor_prueba})) reversa = (5 * 2) + 3 = {resultado}")  # Debería dar 13