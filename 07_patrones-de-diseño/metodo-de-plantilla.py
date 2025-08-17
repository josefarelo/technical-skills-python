from abc import ABC, abstractmethod

class Bebida(ABC):
    def preparar(self):
        self.hervir_agua()
        self.agregar_principal()
        self.agregar_condimentos()
        self.servir()
        self.agregar_extras()

    def hervir_agua(self):
        print("Hirviendo agua por 5 minutos")

    def servir(self):
        print("Sirviendo en taza estándar")

    @abstractmethod
    def agregar_principal(self):
        pass

    def agregar_condimentos(self):
        # Paso opcional que puede ser sobrescrito
        pass

    def agregar_extras(self):
        # Paso opcional que puede ser sobrescrito
        pass

class Cafe(Bebida):
    def agregar_principal(self):
        print("Agregando 2 cucharadas de café molido")

    def agregar_condimentos(self):
        print("Añadiendo un poco de azúcar")

    def agregar_extras(self):
        print("Poniendo una cucharada de crema")

class Te(Bebida):
    def agregar_principal(self):
        print("Colocando bolsita de té verde")

    def agregar_extras(self):
        print("Añadiendo rodaja de limón")

class Chocolate(Bebida):
    def agregar_principal(self):
        print("Disolviendo chocolate en polvo")

    def agregar_condimentos(self):
        print("Agregando canela al gusto")

# Ejemplo
if __name__ == "__main__":
    print("Preparando café:")
    cafe = Cafe()
    cafe.preparar()

    print("\nPreparando té:")
    te = Te()
    te.preparar()

    print("\nPreparando chocolate:")
    chocolate = Chocolate()
    chocolate.preparar()