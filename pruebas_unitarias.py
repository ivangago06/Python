edad = int(input("Ingresa tu edad:"))

assert edad > 18
print("Sigue la ejecución")



from unittest import TestCase

class TestPrueba(TestCase):
  def test_igual(self):
    self.assertEqual("Hola", "Hola")
    self.assertNotEqual("Hola", "hol")
    assert "hola" == "hola"
    assert "hola" != "manteca"



    
from unittest import TestCase

class TestPrueba(TestCase):
    def test_igual(self):
        self.assertEqual("Hola", "Hola")
        self.assertNotEqual("Hola", "hol")
        assert "hola" == "hola"
        assert "hola" != "manteca"

    def test_booleanos(self):
        self.assertTrue("Hola")







        
