"""
Unit tests for web_ramas
"""

import unittest

import requests

from tests.load_env import config


class TestWebRamas(unittest.TestCase):
    """Tests for web_ramas"""

    def test_get_web_ramas(self):
        """Test GET method for web_ramas"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/web_ramas",
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
            self.assertEqual("clave" in item, True)
            self.assertEqual("nombre" in item, True)

    def test_get_web_rama_by_clave(self):
        """Test GET method for web_pagina by clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/web_ramas/noexiste",
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
        self.assertEqual(contenido["success"], False)


if __name__ == "__main__":
    unittest.main()
