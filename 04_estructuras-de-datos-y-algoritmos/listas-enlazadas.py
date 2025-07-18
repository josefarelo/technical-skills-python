class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def imprimir_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    
    def buscar_valor(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    
    def eliminar_nodo(self, valor):
        actual = self.cabeza
        anterior = None
        
        while actual is not None and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        
        if actual is None:
            return False
        
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        return True

# Crear lista y agregar nodos
mi_lista = ListaEnlazada()
mi_lista.agregar_nodo(5)
mi_lista.agregar_nodo(10)
mi_lista.agregar_nodo(15)

# Imprimir lista
print("Lista enlazada:")
mi_lista.imprimir_lista()

# Buscar valor
print("\nBuscar 10:", mi_lista.buscar_valor(10))
print("Buscar 20:", mi_lista.buscar_valor(20))

# Eliminar nodo
print("\nEliminar 10:")
if mi_lista.eliminar_nodo(10):
    print("Nodo eliminado")
else:
    print("Nodo no encontrado")

mi_lista.imprimir_lista()

# Agregar otro nodo
print("\nAgregar 20:")
mi_lista.agregar_nodo(20)
mi_lista.imprimir_lista()