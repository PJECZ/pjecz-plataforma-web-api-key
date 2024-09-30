"""
Unit tests for ubicaciones_expedientes
"""

import unittest

import requests

from tests.load_env import config


class TestUbicacionesExpedientes(unittest.TestCase):
    """Tests for ubicaciones de expedientes category"""

    def test_get_ubicaciones_expedientes(self):
        """Test GET method for ubicaciones_expedientes"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/ubicaciones_expedientes",
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
            self.assertEqual("autoridad_id" in item, True)
            self.assertEqual("autoridad_clave" in item, True)
            self.assertEqual("autoridad_descripcion_corta" in item, True)
            self.assertEqual("expediente" in item, True)
            self.assertEqual("ubicacion" in item, True)

    def test_get_ubicaciones_expedientes_by_autoridad_id(self):
        """Test GET method for ubicaciones_expedientes by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/ubicaciones_expedientes",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37},
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
            self.assertEqual(item["autoridad_id"], 37)

    def test_get_ubicaciones_expedientes_by_autoridad_id_and_expediente(self):
        """Test GET method for ubicaciones_expedientes by autoridad_id and expediente"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/ubicaciones_expedientes",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "expediente": "140/2023"},
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
            self.assertEqual(item["autoridad_id"], 37)

    def test_get_ubicaciones_expedientes_by_autoridad_clave(self):
        """Test GET method for ubicaciones_expedientes by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/ubicaciones_expedientes",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV"},
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
            self.assertEqual(item["autoridad_clave"], "SLT-J2-CIV")

    def test_get_ubicaciones_expedientes_by_autoridad_clave_and_expediente(self):
        """Test GET method for ubicaciones_expedientes by autoridad_clave and expediente"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/ubicaciones_expedientes",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "expediente": "140/2023"},
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
            self.assertEqual(item["autoridad_clave"], "SLT-J2-CIV")

    def test_get_ubicacion_expediente_by_id(self):
        """Test GET method for ubicacion_expediente by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/ubicaciones_expedientes/12",
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
