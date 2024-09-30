"""
Unit tests for permisos
"""

import unittest

import requests

from tests.load_env import config


class TestPermisos(unittest.TestCase):
    """Tests for permisos"""

    def test_get_permisos(self):
        """Test GET method for permisos"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/permisos",
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
            self.assertEqual("modulo_nombre" in item, True)
            self.assertEqual("rol_nombre" in item, True)
            self.assertEqual("nombre" in item, True)
            self.assertEqual("nivel" in item, True)

    def test_get_permiso_by_id(self):
        """Test GET method for permiso by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/permisos/1",
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
