"""
Unit tests for listas de acuerdos
"""

import unittest

import requests

from tests.load_env import config


class TestListasDeAcuerdos(unittest.TestCase):
    """Tests for listas de acuerdos category"""

    def test_get_listas_de_acuerdos(self):
        """Test GET method for listas de acuerdos"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/listas_de_acuerdos",
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

    def test_get_listas_de_acuerdos_by_autoridad_id(self):
        """Test GET method for listas_de_acuerdos by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/listas_de_acuerdos",
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

    def test_get_listas_de_acuerdos_by_autoridad_id_by_fechas(self):
        """Test GET method for listas_de_acuerdos by autoridad_id by fecha_desde by fecha_hasta"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/listas_de_acuerdos",
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

    def test_get_listas_de_acuerdos_by_autoridad_clave_stl_j2_civ(self):
        """Test GET method for listas_de_acuerdos by autoridad_clave SLT-J2-CIV"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/listas_de_acuerdos",
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

    def test_get_listas_de_acuerdos_by_autoridad_clave_stl_j2_civ_by_fechas(self):
        """Test GET method for listas_de_acuerdos by autoridad_clave SLT-J2-CIV fecha_desde 2020-01-01 and fecha_hasta 2020-01-31"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/listas_de_acuerdos",
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

    def test_get_lista_de_acuerdo_by_id(self):
        """Test GET method for lista de acuerdos by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/listas_de_acuerdos/1",
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
