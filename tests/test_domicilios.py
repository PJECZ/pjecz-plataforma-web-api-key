"""
Unit test for domicilios
"""

import unittest

import requests

from tests.load_env import config


class TestDomicilios(unittest.TestCase):
    """Tests for domicilios"""

    def test_get_domicilios(self):
        """Test GET method for domicilios"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/domicilios",
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
            self.assertEqual("edificio" in item, True)

    def test_get_domicilio_by_id(self):
        """Test GET method for domicilios by id 18"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/domicilios/18",
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
        self.assertEqual("edificio" in contenido, True)
        self.assertEqual("estado" in contenido, True)
        self.assertEqual("municipio" in contenido, True)
        self.assertEqual("calle" in contenido, True)
        self.assertEqual("num_ext" in contenido, True)
        self.assertEqual("num_int" in contenido, True)
        self.assertEqual("colonia" in contenido, True)
        self.assertEqual("cp" in contenido, True)
        self.assertEqual("completo" in contenido, True)

    def test_get_domicilio_by_id(self):
        """Test GET method for domicilio by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/domicilios/1",
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
