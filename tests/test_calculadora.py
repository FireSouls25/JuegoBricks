import unittest
from src.calculadora import suma

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)
    
    def test_suma_mixto(self):
        self.assertEqual(suma(-2, 3), 1)
    
    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)
    
if __name__ == "__main__":
    unittest.main()
