"""
Unit tests for edictos
"""

import unittest

import requests

from tests.load_env import config


class TestEdictos(unittest.TestCase):
    """Tests for edictos"""

    def test_get_edictos(self):
        """Test GET method for edictos"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
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
            self.assertEqual("descripcion" in item, True)
            self.assertEqual("expediente" in item, True)
            self.assertEqual("numero_publicacion" in item, True)

    def test_get_edictos_by_autoridad_id(self):
        """Test GET method for edictos by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
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

    def test_get_edictos_by_autoridad_id_by_fechas(self):
        """Test GET method for edictos by autoridad_id by fecha_desde by fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "fecha_desde": "2020-01-01", "fecha_hasta": "2020-01-31"},
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
            self.assertGreaterEqual(item["fecha"], "2020-01-01")
            self.assertLessEqual(item["fecha"], "2020-01-31")

    def test_get_edictos_by_autoridad_id_and_expediente(self):
        """Test GET method for edictos by autoridad_id by expediente"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 35, "expediente": "1774/2019"},
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
            self.assertEqual(item["autoridad_id"], 35)
            self.assertEqual(item["expediente"], "1774/2019")

    def test_get_edictos_by_autoridad_clave(self):
        """Test GET method for edictos by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
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

    def test_get_edictos_by_autoridad_clave_by_fechas(self):
        """Test GET method for edictos by autoridad_clave by fecha_desde by fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "fecha_desde": "2020-01-01", "fecha_hasta": "2020-01-31"},
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
            self.assertGreaterEqual(item["fecha"], "2020-01-01")
            self.assertLessEqual(item["fecha"], "2020-01-31")

    def test_get_edictos_by_autoridad_clave_and_expediente(self):
        """Test GET method for edictos by autoridad_clave by expediente"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J1-FAM", "expediente": "1774/2019"},
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
            self.assertEqual(item["autoridad_clave"], "SLT-J1-FAM")
            self.assertEqual(item["expediente"], "1774/2019")

    def test_get_edicto_by_id(self):
        """Test GET method for edicto by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/edictos/1",
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
