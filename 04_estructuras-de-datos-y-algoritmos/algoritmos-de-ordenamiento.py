def bubble_sort(lista):

    n = len(lista)
    for i in range(n):
        swapped = False  # Bandera para optimización
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break

def main():
    # Pruebas del algoritmo
    datos1 = [5, 2, 9, 1, 5, 6]
    print("Lista original 1:", datos1)
    bubble_sort(datos1)
    print("Lista ordenada 1:", datos1)
    
    datos2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("\nLista original 2:", datos2)
    bubble_sort(datos2)
    print("Lista ordenada 2:", datos2)
    
    datos3 = [1, 2, 3, 4, 5]  # Lista ya ordenada
    print("\nLista original 3:", datos3)
    bubble_sort(datos3)
    print("Lista ordenada 3:", datos3)

if __name__ == "__main__":
    main()