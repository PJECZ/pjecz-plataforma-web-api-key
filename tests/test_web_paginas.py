"""
Unit tests for web_paginas
"""

import unittest

import requests

from tests.load_env import config


class TestWebPaginas(unittest.TestCase):
    """Tests for web_paginas"""

    def test_get_web_paginas(self):
        """Test GET method for web_paginas"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/web_paginas",
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
            self.assertEqual("clave" in item, True)
            self.assertEqual("titulo" in item, True)
            self.assertEqual("resumen" in item, True)
            self.assertEqual("ruta" in item, True)
            self.assertEqual("fecha_modificacion" in item, True)
            self.assertEqual("responsable" in item, True)
            self.assertEqual("etiquetas" in item, True)
            self.assertEqual("vista_previa" in item, True)
            self.assertEqual("estado" in item, True)

    def test_get_web_pagina_by_clave(self):
        """Test GET method for web_pagina by clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/web_paginas/noexiste",
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
