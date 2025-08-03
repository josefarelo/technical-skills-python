# Malos nombres
def calc(x, y):
    return x + y * 2

def proc(lst):
    temp = []
    for i in lst:
        if i % 2 == 0:
            temp.append(i)
    return temp

# Mejores nombres
def calcular_total_con_impuesto(subtotal: float, tasa_impuesto: float) -> float:
    return subtotal + (subtotal * tasa_impuesto)

def filtrar_numeros_pares(numeros: list) -> list:
    numeros_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

# Ejemplo
if __name__ == "__main__":
    # Uso con malos nombres
    resultado1 = calc(100, 0.15)
    lista1 = proc([1, 2, 3, 4, 5, 6])
    
    print(f"Resultado cálculo (malos nombres): {resultado1}")
    print(f"Lista filtrada (malos nombres): {lista1}")
    
    # Uso con buenos nombres
    total_con_impuesto = calcular_total_con_impuesto(100, 0.15)
    numeros_pares = filtrar_numeros_pares([1, 2, 3, 4, 5, 6])
    
    print(f"\nTotal con impuesto (buenos nombres): {total_con_impuesto}")
    print(f"Números pares (buenos nombres): {numeros_pares}")