# Pedir al usuario que ingrese un número
numero = input("Por favor, ingresa un número entero: ")

# Verificar si el input es un número válido
while not numero.isdigit():
    print("¡Eso no es un número válido!")
    numero = input("Intenta de nuevo, ingresa un número entero: ")

# Convertir el input a entero
numero = int(numero)

# Comprobar si es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Imprimir números del 1 al 10
print("\nAhora vamos a imprimir los números del 1 al 10:")
for i in range(1, 11):
    print(i, end=' ')  

print("\n\n¡Fin del programa!")