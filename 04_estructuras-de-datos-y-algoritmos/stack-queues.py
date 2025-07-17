# Implementación básica de Stack
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
        print(f"Elemento {item} apilado")
    
    def desapilar(self):
        if not self.esta_vacia():
            item = self.items.pop()
            print(f"Elemento {item} desapilado")
            return item
        else:
            print("La pila está vacía")
            return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print("La pila está vacía")
            return None

# Implementación básica de Queue
from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()
    
    def encolar(self, item):
        self.items.append(item)
        print(f"Elemento {item} encolado")
    
    def desencolar(self):
        if not self.esta_vacia():
            item = self.items.popleft()
            print(f"Elemento {item} desencolado")
            return item
        else:
            print("La cola está vacía")
            return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)
    
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            print("La cola está vacía")
            return None

# Demostración de uso
print("=== Demostración de Pila ===")
mi_pila = Pila()
mi_pila.apilar(10)
mi_pila.apilar(20)
mi_pila.apilar(30)
print("Tamaño de la pila:", mi_pila.tamano())
print("Tope de la pila:", mi_pila.ver_tope())
mi_pila.desapilar()
mi_pila.desapilar()
print("La pila está vacía?", mi_pila.esta_vacia())

print("\n=== Demostración de Cola ===")
mi_cola = Cola()
mi_cola.encolar("a")
mi_cola.encolar("b")
mi_cola.encolar("c")
print("Tamaño de la cola:", mi_cola.tamano())
print("Frente de la cola:", mi_cola.ver_frente())
mi_cola.desencolar()
mi_cola.desencolar()
print("La cola está vacía?", mi_cola.esta_vacia())