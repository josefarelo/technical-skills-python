class Carrito:
    def __init__(self):
        self.items = []
    
    def agregar(self, item, precio):
        self.items.append((item, precio))
    
    def total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
    def vaciar(self):
        self.items = []