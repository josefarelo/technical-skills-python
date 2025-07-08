def duplicar_lista(lista_original):
    # Crear una nueva lista para no modificar la original
    lista_duplicada = []
    
    # Recorrer cada elemento y duplicarlo
    for numero in lista_original:
        lista_duplicada.append(numero * 2)
    
    return lista_duplicada

# Lista original que no debe modificarse
numeros = [5, 10, 15, 20]

# Llamar a la función para crear la nueva lista
resultado = duplicar_lista(numeros)

# Mostrar ambos resultados para demostrar inmutabilidad
print("Lista original (no modificada):", numeros)
print("Nueva lista con valores duplicados:", resultado)

# Verificación adicional para demostrar que son objetos diferentes
print("¿Son el mismo objeto en memoria?", numeros is resultado)