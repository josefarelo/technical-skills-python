import unittest
from prod import suma

class TestSuma(unittest.TestCase):
    
    def test_suma_basica(self):
        resultado = suma(2, 3)
        self.assertEqual(resultado, 5)
        print("Test básico pasado: 2 + 3 = 5")
    
    def test_suma_negativos(self):
        resultado = suma(-2, -3)
        self.assertEqual(resultado, -5)
        print("Test negativos pasado: -2 + (-3) = -5")
    
    def test_suma_cero(self):
        resultado = suma(0, 5)
        self.assertEqual(resultado, 5)
        print("Test cero pasado: 0 + 5 = 5")
    
    def test_suma_decimales(self):
        resultado = suma(2.5, 3.1)
        self.assertAlmostEqual(resultado, 5.6)
        print("Test decimales pasado: 2.5 + 3.1 ≈ 5.6")
    
    def test_suma_grandes(self):
        resultado = suma(1000000, 2000000)
        self.assertEqual(resultado, 3000000)
        print("Test números grandes pasado: 1,000,000 + 2,000,000 = 3,000,000")

if __name__ == "__main__":
    unittest.main(verbosity=2)