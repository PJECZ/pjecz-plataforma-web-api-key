"""
Unit tests for oficinas
"""

import unittest

import requests

from tests.load_env import config


class TestOficinas(unittest.TestCase):
    """Tests for oficinas category"""

    def test_get_oficinas(self):
        """Test GET method for oficinas"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/oficinas",
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
        self.assertEqual("pages" in contenido, True)
        self.assertEqual("size" in contenido, True)
        self.assertEqual("total" in contenido, True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual("id" in item, True)
            self.assertEqual("distrito_clave" in item, True)
            self.assertEqual("distrito_nombre_corto" in item, True)
            self.assertEqual("domicilio_edificio" in item, True)
            self.assertEqual("clave" in item, True)
            self.assertEqual("descripcion_corta" in item, True)
            self.assertEqual("es_jurisdiccional" in item, True)

    def test_get_oficina_by_clave(self):
        """Test GET method for oficina by clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/oficinas/dsal04-dinfo",
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
