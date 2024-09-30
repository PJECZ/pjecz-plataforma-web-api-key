"""
Unit tests for materias_tipos_juicios
"""

import unittest

import requests

from tests.load_env import config


class TestMateriasTiposJuicios(unittest.TestCase):
    """Tests for materias-tipos juicios category"""

    def test_get_materias_tipos_juicios(self):
        """Test GET method for materias_tipos_juicios"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/materias_tipos_juicios",
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
            self.assertEqual("materia_clave" in item, True)
            self.assertEqual("materia_nombre" in item, True)
            self.assertEqual("descripcion" in item, True)

    def test_get_materia_tipo_juicio_by_id(self):
        """Test GET method for materia_tipo_juicio by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/materias_tipos_juicios/1",
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
