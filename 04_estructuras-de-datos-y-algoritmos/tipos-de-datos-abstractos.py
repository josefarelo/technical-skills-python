from abc import ABC, abstractmethod

class PilaAbstracta(ABC):
    @abstractmethod
    def push(self, elemento):
        """Añade un elemento a la pila"""
        pass
    
    @abstractmethod
    def pop(self):
        """Elimina y devuelve el elemento superior de la pila"""
        pass
    
    @abstractmethod
    def esta_vacia(self):
        """Comprueba si la pila está vacía"""
        pass
    
    @abstractmethod
    def ver_tope(self):
        """Muestra el elemento superior sin eliminarlo"""
        pass

class PilaLista(PilaAbstracta):
    def __init__(self):
        self.items = []
    
    def push(self, elemento):
        self.items.append(elemento)
    
    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

# Pruebas
if __name__ == "__main__":
    mi_pila = PilaLista()
    
    print("¿Está vacía?", mi_pila.esta_vacia())
    mi_pila.push("primero")
    mi_pila.push("segundo")
    
    print("Tope actual:", mi_pila.ver_tope())
    print("¿Está vacía?", mi_pila.esta_vacia())
    
    print("Pop:", mi_pila.pop())
    print("Pop:", mi_pila.pop())
    
    try:
        mi_pila.pop()
    except IndexError as e:
        print("Error:", e)