def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Probamos la función con diferentes valores
print("Factorial de 5:", factorial(5))  # Debería dar 120
print("Factorial de 3:", factorial(3))  # Debería dar 6
print("Factorial de 0:", factorial(0))  # Debería dar 1

# Pedimos un número al usuario para calcular su factorial
try:
    num = int(input("Ingresa un número para calcular su factorial: "))
    if num < 0:
        print("El factorial no está definido para números negativos.")
    else:
        print(f"El factorial de {num} es: {factorial(num)}")
except ValueError:
    print("Por favor ingresa un número válido.")