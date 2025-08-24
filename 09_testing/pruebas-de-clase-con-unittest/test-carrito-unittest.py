import unittest
from carrito import Carrito

class TestCarrito(unittest.TestCase):
    def setUp(self):
        self.carrito = Carrito()
        self.carrito.agregar("lapiz", 100)
        print("Se ejecutó setUp - carrito creado con un lápiz")
    
    def tearDown(self):
        self.carrito.vaciar()
        print("Se ejecutó tearDown - carrito vaciado")
    
    def test_total_inicial(self):
        print("Ejecutando test_total_inicial...")
        resultado = self.carrito.total()
        self.assertEqual(resultado, 100)
        print(f"Total inicial: {resultado}")
    
    def test_agregar_item_incrementa_total(self):
        print("Ejecutando test_agregar_item_incrementa_total...")
        self.carrito.agregar("cuaderno", 300)
        resultado = self.carrito.total()
        self.assertEqual(resultado, 400)
        print(f"Total después de agregar cuaderno: {resultado}")
    
    def test_agregar_varios_items(self):
        print("Ejecutando test_agregar_varios_items...")
        self.carrito.agregar("goma", 50)
        self.carrito.agregar("regla", 150)
        resultado = self.carrito.total()
        self.assertEqual(resultado, 300)
        print(f"Total después de agregar goma y regla: {resultado}")
    
    def test_vaciar_carrito(self):
        print("Ejecutando test_vaciar_carrito...")
        self.carrito.vaciar()
        resultado = self.carrito.total()
        self.assertEqual(resultado, 0)
        print(f"Total después de vaciar: {resultado}")

if __name__ == "__main__":
    unittest.main()