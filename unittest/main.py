from unittest import TestCase

from unittest.mock import patch

from prueba import ejecutar_magia

class TestMock(TestCase):
    @patch("prueba.magia")
    def test_magia(self, mock):
        respuesta=ejecutar_magia()
        print(respuesta)
