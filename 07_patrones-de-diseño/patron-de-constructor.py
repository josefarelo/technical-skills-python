class PizzaBuilder:
    def __init__(self):
        self.ingredientes = []
        self.tamano = "mediana"
        self.masa = "normal"
        self.queso_extra = False

    def agregar_ingrediente(self, ingrediente):
        if ingrediente.lower() not in [i.lower() for i in self.ingredientes]:
            self.ingredientes.append(ingrediente)
        else:
            print(f"El ingrediente {ingrediente} ya está añadido.")
        return self

    def set_tamano(self, tamano):
        tamanos_validos = ["pequena", "mediana", "grande"]
        if tamano.lower() in tamanos_validos:
            self.tamano = tamano.lower()
        else:
            print(f"Tamaño no válido. Usando tamaño por defecto ({self.tamano})")
        return self

    def set_masa(self, tipo_masa):
        masas_validas = ["normal", "fina", "gruesa"]
        if tipo_masa.lower() in masas_validas:
            self.masa = tipo_masa.lower()
        else:
            print(f"Tipo de masa no válido. Usando masa por defecto ({self.masa})")
        return self

    def agregar_queso_extra(self):
        self.queso_extra = True
        return self

    def build(self):
        return Pizza(self.ingredientes, self.tamano, self.masa, self.queso_extra)

class Pizza:
    def __init__(self, ingredientes, tamano, masa, queso_extra):
        self.ingredientes = ingredientes
        self.tamano = tamano
        self.masa = masa
        self.queso_extra = queso_extra

    def mostrar_pizza(self):
        print("\nDetalles de tu pizza:")
        print(f"- Tamaño: {self.tamano}")
        print(f"- Masa: {self.masa}")
        print(f"- Queso extra: {'Sí' if self.queso_extra else 'No'}")
        print("- Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"  * {ingrediente}")

# Ejemplo
if __name__ == "__main__":
    builder = PizzaBuilder()
    pizza = (builder
        .set_tamano("grande")
        .set_masa("fina")
        .agregar_ingrediente("jamón")
        .agregar_ingrediente("champiñones")
        .agregar_ingrediente("jamón")  # Este ya está añadido
        .agregar_queso_extra()
        .build())

    pizza.mostrar_pizza()