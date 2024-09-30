"""
Unit tests for glosas
"""

import unittest

import requests

from tests.load_env import config


class TestGlosas(unittest.TestCase):
    """Tests for glosas category"""

    def test_get_glosas(self):
        """Test GET method for glosas"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/glosas",
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
            self.assertEqual("autoridad_id" in item, True)
            self.assertEqual("autoridad_clave" in item, True)
            self.assertEqual("autoridad_descripcion_corta" in item, True)
            self.assertEqual("fecha" in item, True)
            self.assertEqual("tipo_juicio" in item, True)
            self.assertEqual("descripcion" in item, True)
            self.assertEqual("expediente" in item, True)

    def test_get_glosas_by_autoridad_id_(self):
        """Test GET method for glosas by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/glosas",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 53},
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
            self.assertEqual(item["autoridad_id"], 53)

    def test_get_glosas_by_autoridad_id_by_fechas(self):
        """Test GET method for glosas by autoridad_id by fecha_desde by fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/glosas",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 53, "fecha_desde": "2020-01-01", "fecha_hasta": "2020-01-31"},
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
            self.assertEqual(item["autoridad_id"], 53)
            self.assertGreaterEqual(item["fecha"], "2020-01-01")
            self.assertLessEqual(item["fecha"], "2020-01-31")

    def test_get_glosas_by_autoridad_clave(self):
        """Test GET method for glosas by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/glosas",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "TRN-CYA"},
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
            self.assertEqual(item["autoridad_clave"], "TRN-CYA")

    def test_get_glosas_by_autoridad_clave_by_fechas(self):
        """Test GET method for glosas by autoridad_clave by fecha_desde by fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/glosas",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "TRN-CYA", "fecha_desde": "2020-01-01", "fecha_hasta": "2020-01-31"},
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
            self.assertEqual(item["autoridad_clave"], "TRN-CYA")
            self.assertGreaterEqual(item["fecha"], "2020-01-01")
            self.assertLessEqual(item["fecha"], "2020-01-31")

    def test_get_glosa_by_id(self):
        """Test GET method for glosa by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/glosas/1",
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
