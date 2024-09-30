"""
Unit tests for audiencias
"""

import unittest

import requests

from tests.load_env import config


class TestAudiencias(unittest.TestCase):
    """Tests for audiencias"""

    def test_get_audiencias(self):
        """Test GET method for audiencias"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/audiencias",
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
            self.assertEqual("tiempo" in item, True)
            self.assertEqual("tipo_audiencia" in item, True)
            self.assertEqual("expediente" in item, True)
            self.assertEqual("actores" in item, True)
            self.assertEqual("demandados" in item, True)
            self.assertEqual("sala" in item, True)
            self.assertEqual("caracter" in item, True)
            self.assertEqual("causa_penal" in item, True)
            self.assertEqual("delitos" in item, True)
            self.assertEqual("toca" in item, True)
            self.assertEqual("expediente_origen" in item, True)
            self.assertEqual("imputados" in item, True)
            self.assertEqual("origen" in item, True)

    def test_get_audiencias_by_autoridad_id(self):
        """Test GET method for audiencias by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/audiencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 35},
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

    def test_get_audiencias_by_autoridad_id_by_fecha(self):
        """Test GET method for audiencias by autoridad_id by fecha"""
        response = requests.get(
            url=f"{config['api_base_url']}/audiencias",
            headers={"X-Api-Key": config["api_key"]},
            params={"autoridad_id": 35, "fecha": "2023-05-11"},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_id"], 35)
            self.assertEqual(item["tiempo"].split("T")[0], "2023-05-11")

    def test_get_audiencias_by_autoridad_clave(self):
        """Test GET method for audiencias by autoridad_clave"""
        response = requests.get(
            url=f"{config['api_base_url']}/audiencias",
            headers={"X-Api-Key": config["api_key"]},
            params={"autoridad_clave": "SLT-J1-FAM"},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_clave"], "SLT-J1-FAM")

    def test_get_audiencias_by_autoridad_clave_by_fecha(self):
        """Test GET method for audiencias by autoridad_id by fecha"""
        response = requests.get(
            url=f"{config['api_base_url']}/audiencias",
            headers={"X-Api-Key": config["api_key"]},
            params={"autoridad_clave": "SLT-J1-FAM", "fecha": "2023-05-11"},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual(contenido["success"], True)
        self.assertEqual("items" in contenido, True)
        for item in contenido["items"]:
            self.assertEqual(item["autoridad_clave"], "SLT-J1-FAM")
            self.assertEqual(item["tiempo"].split("T")[0], "2023-05-11")

    def test_get_audiencia_by_id(self):
        """Test GET method for audiencia by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/audiencias/1",
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
