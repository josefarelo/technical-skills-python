def multiplicar(a):
    def por(b):
        def por_ultimo(c):
            return a * b * c
        return por_ultimo
    return por

# Ejemplo de uso
multiplicar_por_2 = multiplicar(2)
multiplicar_por_2_y_3 = multiplicar_por_2(3)
resultado = multiplicar_por_2_y_3(4)  # 2 * 3 * 4 = 24
print(resultado)

# También se puede llamar directamente
print(multiplicar(2)(3)(4))  # 24

# Otra función con currying para demostración
def concatenar(a):
    def con(b):
        def con_ultimo(c):
            return f"{a} {b} {c}"
        return con_ultimo
    return con

# Uso
saludo = concatenar("Hola")("Mundo")("!")
print(saludo)  # "Hola Mundo !"

# Función más simple con un solo nivel de currying
def potencia(exponente):
    def aplicar(base):
        return base ** exponente
    return aplicar

cuadrado = potencia(2)
cubo = potencia(3)

print(cuadrado(5))  # 25
print(cubo(3))      # 27