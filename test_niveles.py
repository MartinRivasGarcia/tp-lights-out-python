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


class test_validar_coordenadas(unittest.TestCase):

    def test_envioUnaCoordenadaValida_a3_deberiaDevolver_True(self):
        self.assertTrue(niveles.validar_coordenadas_ingresadas("a3",5))

    def test_envioUnaCoordenadaMayorAlTamaño_e7_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("e7",5))

    def test_envioUnaCoordenadaMayorAlTamaño_3a_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("3a",5))

    def test_envioUnaCoordenadaVacia_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("", 5))

    def test_envioUnaCoordenadaConDosNumeros_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("33", 5))

    def test_envioUnaCoordenadaConDosLetras_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("bb", 5))

    def test_envioUnaCoordenadaConEspacios_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("  ", 5))

    def test_envioUnaCoordenadaConMuchosCaracteres_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("adf45r1z2s", 5))

    def test_envioUnaCoordenadaConEspacioIntermedio_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("a 3", 5))

    def test_envioUnaCoordenadaConEspacioAlInicio_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas(" a3", 5))

    def test_envioUnaCoordenadaConEspacioAlFinal_deberiaDevolver_False(self):
        self.assertFalse(niveles.validar_coordenadas_ingresadas("a3 ", 5))


class test_limite(unittest.TestCase):
    def test_IngresoTamañoValido_deveriaDevolverTupla(self):
        self.assertEqual(niveles.limite(2), ('b', 'B'))

    def test_IngresoTamañoInvalido_deveriaDevolverTupla00(self):
        self.assertEqual(niveles.limite(11), (0, 0))

    def test_IngresoTamañoVacio_deveriaDevolverTupla00(self):
        self.assertEqual(niveles.limite(""), (0, 0))

    def test_IngresoTamañoConLetras_deveriaDevolverTupla00(self):
        self.assertEqual(niveles.limite("aa"), (0, 0))

    def test_IngresoTamañoConEspacios_deveriaDevolverTupla00(self):
        self.assertEqual(niveles.limite("  "), (0, 0))

    def test_IngresoTamañoCero_deveriaDevolverTupla00(self):
        self.assertEqual(niveles.limite(0), (0, 0))

    def test_IngresoTamañoNegativo_deveriaDevolverTupla00(self):
        self.assertEqual(niveles.limite(-1), (0, 0))


class test_devolverTabler(unittest.TestCase):
    def test_IngresoNivelValido_deveriaDevolverNivelCorrespondiente(self):
        self.assertEqual(niveles.devolverTablero(1), [['0','0','.','0','0'],['0','.','0','.','0'],['.','0','0','0','.'],['0','.','0','.','0'],['0','0','.','0','0']])

    def test_IngresoNivelInvalido_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero(9))

    def test_IngresoNivelCero_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero(0))

    def test_IngresoNivelLetra_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero('a'))

    def test_IngresoNivelConEspacio_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero(' '))

    def test_IngresoNivelVacio_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero(''))

    def test_IngresoNivelConPunto_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero('.'))

    def test_IngresoNivelConNumerosDeMas_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero(75624))

    def test_IngresoNivelConCaracteresDeMas_deveriaDevolverFalse(self):
        self.assertFalse(niveles.devolverTablero('abcdefg'))