"""
Unit tests for redam (Registro Estatal de Deudores Alimentarios Morosos)
"""

import unittest

import requests

from tests.load_env import config


class TestREDAM(unittest.TestCase):
    """Tests for redam"""

    def test_get_redam(self):
        """Test GET method for redam"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/redam",
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
            self.assertEqual("distrito_id" in item, True)
            self.assertEqual("distrito_clave" in item, True)
            self.assertEqual("distrito_nombre_corto" in item, True)
            self.assertEqual("autoridad_id" in item, True)
            self.assertEqual("autoridad_clave" in item, True)
            self.assertEqual("autoridad_descripcion_corta" in item, True)
            self.assertEqual("nombre" in item, True)
            self.assertEqual("expediente" in item, True)
            self.assertEqual("fecha" in item, True)
            self.assertEqual("observaciones" in item, True)

    def test_get_redam_by_distrito_id(self):
        """Test GET method for redam by distrito_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/redam",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6},
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
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)

    def test_get_redam_by_distrito_id_by_nombre(self):
        """Test GET method for redam by distrito_id by nombre"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/redam",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6, "nombre": "LUIS"},
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
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_id"], 6)
            self.assertIn("LUIS", item["nombre"])

    def test_get_redam_by_distrito_clave(self):
        """Test GET method for redam by distrito_clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/redam",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC"},
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
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")

    def test_get_redam_by_distrito_clave_by_nombre(self):
        """Test GET method for redam by distrito_clave by nombre"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/redam",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC", "nombre": "LUIS"},
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
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["distrito_clave"], "DTRC")
            self.assertIn("LUIS", item["nombre"])

    def test_get_redam_by_id(self):
        """Test GET method for redam by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/redam/999999",
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
