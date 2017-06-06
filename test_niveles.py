import niveles
import unittest

class test_coordenadas_coonvetidas(unittest.TestCase):

    def test_envio_a_deberiaDevolver0(self):
        print("pepe")
        self.assertEquals((0,0),niveles.convertir_coordenadas("a1",5))

    def test_envioCoordenadaIncorrecta1a_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("1a",5))

    def test_envioCoordenadaStringVacio_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("", 5))

    def test_envioCoordenadaTamañoNulo_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("a1", 0))

    def test_envioDeFilasIgualACero_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("a0",5))

    def test_envioDeCoordenadaValida_e5_debriaDevolver_44(self):
        self.assertEqual((4,4),niveles.convertir_coordenadas("e5",5))

    def test_envioUnaCoordendaValidaParaOtroTamaño_deberiaDevolverFalse(self):
        self.assertFalse(niveles.convertir_coordenadas("d6",4))

    def test_envioUnaCoordendaValidaParaUnTamañoMuyChico_deberiaDevolver_20(self):
        self.assertEquals((2,0),niveles.convertir_coordenadas("a3",4))

    def test_envioUnaCoordendaValidaParaUnTamañoMuyGrande_deberiaDevolver_False(self):
        self.assertFalse(niveles.convertir_coordenadas("a3",11))


class test_validar_coordenadas(unittest.TestCase): #no me esta corriendo estas pruebas

    def test_envioUnaCoordenadaValida_a3_deberiaDevolver_True(self):
        print("carlos")
        self.assertTrue(niveles.validar_coordenadas_ingresadas("a3",5))

    def test_envioUnaCoordenadaMayorAlTamaño_e7_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("e7",5))