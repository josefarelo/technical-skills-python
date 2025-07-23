def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Pruebas de las funciones
datos_ordenados = [1, 3, 4, 6, 8, 9, 11]
datos_desordenados = [9, 1, 6, 3, 11, 4, 8]

print("--- Pruebas de búsqueda binaria (lista ordenada) ---")
print(f"Posición del 6: {busqueda_binaria(datos_ordenados, 6)}")  # 3
print(f"Posición del 10: {busqueda_binaria(datos_ordenados, 10)}")  # -1

print("\n--- Pruebas de búsqueda lineal (lista desordenada) ---")
print(f"Posición del 6: {busqueda_lineal(datos_desordenados, 6)}")  # 2
print(f"Posición del 10: {busqueda_lineal(datos_desordenados, 10)}")  # -1

# Comparación de rendimiento
import time

lista_grande = list(range(1, 1000001))
objetivo = 999999

inicio = time.time()
resultado_bin = busqueda_binaria(lista_grande, objetivo)
tiempo_bin = time.time() - inicio

inicio = time.time()
resultado_lin = busqueda_lineal(lista_grande, objetivo)
tiempo_lin = time.time() - inicio

print("\n--- Comparación de rendimiento en lista grande ---")
print(f"Búsqueda binaria: {tiempo_bin:.6f} segundos")
print(f"Búsqueda lineal: {tiempo_lin:.6f} segundos")