import niveles
import unittest

class test_coordenadas_coonvetidas(unittest.TestCase):
    def test_envio_a_deberiaDevolver0(self):
        self.assertEquals((0,0),niveles.convertir_coordenadas("a1",5))

    def test_envioCoordenadaIncorrecta1a_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("1a",5))

    def test_envioCoordenadaStringVacio_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("", 5))

    def test_envioCoordenadaTamañoNulo_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("a1", 0))