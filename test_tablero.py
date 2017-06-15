import unittest
import tablero

class test_verificar_tablero_ganado(unittest.TestCase):
    def test_envioUnaGrillaInicialTamaño5_DeberiaDevolverFalse(self):
        self.assertFalse(tablero.verificarJuegoGanado( [['0','0','.','0','0'],['0','.','0','.','0'],['.','0','0','0','.'],['0','.','0','.','0'],['0','0','.','0','0']],5))

    def test_envioUnaGrillaInicialTamaño3PeroDatoErroneoDeTamaño_DeberiaDevolverFalse(self):
        self.assertFalse(tablero.verificarJuegoGanado([['.', '0', '0', '0', '.'], ['0', '.', '0', '.', '0'],['0', '0', '.', '0', '0']], 5))

    def test_envioUnaGrillaConPuntos_DeberiaDevolverTrue(self):
        self.assertTrue(tablero.verificarJuegoGanado([['.', '.', '.'], ['.', '.', '.'],['.', '.', '.']], 3))

    def test_envioUnaGrillaInvalidaConCaracteres_DeberiaDevolverFalse(self):
        self.assertFalse(tablero.verificarJuegoGanado([['A', '0', '.'], ['R', ' ', '.'],['.', '.', '.']], 3))

    def test_envioUnaGrillaVacia_DeberiaDevolverFalse(self):
        self.assertFalse(tablero.verificarJuegoGanado(['0'], 1))

class test_interactuarConElTablero(unittest.TestCase):

    def test_EnvioCoordendasInvalidadas_DeberiaDevolverFalse(self):
        self.assertFalse(tablero.interactuar_con_el_tablero("77")

    def test_EnvioCoordendasValidadas_DeberiaModificarmeElTablero(self):
        tablero.inicializarTablero(5)
        tablero.interactuar_con_el_tablero("a1")
        grilla = tablero.tablero
        print(grilla)
        #self.assertEquals(grilla,[['.','.','.','0','0'],['.','.','0','.','0'],['.','0','0','0','.'],['0','.','0','.','0'],['0','0','.','0','0']])