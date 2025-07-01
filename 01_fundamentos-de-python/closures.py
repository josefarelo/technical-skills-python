def crear_sumador(numero_fijo):
    #Crea una función que suma un número fijo a cualquier número que se le pase.
        sumar5 = crear_sumador(5)
        sumar5(3)  # Devuelve 8
        
    def sumar(numero):
        resultado = numero_fijo + numero
        return resultado
    
    return sumar

# Ejemplos de uso
sumar10 = crear_sumador(10)
print("10 + 5 =", sumar10(5))  # 15

sumar25 = crear_sumador(25)
print("25 + 10 =", sumar25(10))  # 35

# Probamos que el closure mantiene su estado
mismo_sumador = sumar10
print("Usando el mismo closure otra vez (10 + 8):", mismo_sumador(8))  # 18

# Probamos con números negativos
restar5 = crear_sumador(-5)
print("-5 + 20 =", restar5(20))  # 15

# Probamos con floats
sumar3_5 = crear_sumador(3.5)
print("3.5 + 2.1 =", sumar3_5(2.1))  # 5.6