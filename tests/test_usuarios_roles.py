"""
Unit tests for usuarios_roles
"""

import unittest

import requests

from tests.load_env import config


class TestUsuariosRoles(unittest.TestCase):
    """Tests for usuarios_roles"""

    def test_get_usuarios_roles(self):
        """Test GET method for usuarios_roles"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/usuarios_roles",
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
            self.assertEqual("rol_nombre" in item, True)
            self.assertEqual("usuario_email" in item, True)
            self.assertEqual("descripcion" in item, True)

    def test_get_usuario_rol_by_id(self):
        """Test GET method for usuario_rol by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/usuarios_roles/1",
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
