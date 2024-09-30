"""
Unit tests for peritos_tipos
"""

import unittest

import requests

from tests.load_env import config


class TestPeritosTipos(unittest.TestCase):
    """Tests for peritos_tipos"""

    def test_get_peritos_tipos(self):
        """Test GET method for peritos_tipos"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos_tipos",
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
            self.assertEqual("nombre" in item, True)

    def test_get_perito_tipo_by_id(self):
        """Test GET method for perito_tipo by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos_tipos/1",
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
