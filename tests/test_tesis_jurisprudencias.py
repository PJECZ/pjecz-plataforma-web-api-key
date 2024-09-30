"""
Unit tests for tesis_jurisprudencias
"""

import unittest

import requests

from tests.load_env import config


class TestTesisJurisprudencias(unittest.TestCase):
    """Tests for tesis_jurisprudencias category"""

    def test_get_tesis_jurisprudencias(self):
        """Test GET method for tesis_jurisprudencias"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/tesis_jurisprudencias",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual("message" in contenido, True)
        self.assertEqual("total" in contenido, True)
        self.assertEqual("limit" in contenido, True)
        self.assertEqual("offset" in contenido, True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual("id" in item, True)
            self.assertEqual("distrito_clave" in item, True)
            self.assertEqual("distrito_nombre_corto" in item, True)
            self.assertEqual("autoridad_clave" in item, True)
            self.assertEqual("autoridad_descripcion_corta" in item, True)
            self.assertEqual("epoca_nombre" in item, True)
            self.assertEqual("materia_clave" in item, True)
            self.assertEqual("materia_nombre" in item, True)
            self.assertEqual("titulo" in item, True)
            self.assertEqual("subtitulo" in item, True)
            self.assertEqual("tipo" in item, True)
            self.assertEqual("estado" in item, True)
            self.assertEqual("clave_control" in item, True)
            self.assertEqual("clase" in item, True)
            self.assertEqual("rubro" in item, True)

    def test_get_tesis_jurisprudencia_by_id(self):
        """Test GET method for tesis_jurisprudencia by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/tesis_jurisprudencias/1",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)


if __name__ == "__main__":
    unittest.main()
