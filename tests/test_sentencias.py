"""
Unit tests for sentencias
"""

import unittest

import requests

from tests.load_env import config


class TestSentencias(unittest.TestCase):
    """Tests for sentencias category"""

    def test_get_sentencias(self):
        """Test GET method for sentencias"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
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
            self.assertEqual("materia_nombre" in item, True)
            self.assertEqual("materia_tipo_juicio_descripcion" in item, True)
            self.assertEqual("sentencia" in item, True)
            self.assertEqual("sentencia_fecha" in item, True)
            self.assertEqual("expediente" in item, True)
            self.assertEqual("fecha" in item, True)
            self.assertEqual("descripcion" in item, True)
            self.assertEqual("es_perspectiva_genero" in item, True)

    def test_get_sentencias_by_autoridad_id(self):
        """Test GET method for sentencias by autoridad_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
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

    def test_get_sentencias_by_autoridad_id_by_expediente(self):
        """Test GET method for sentencias by autoridad_id by expediente"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "expediente_anio": 2019, "expediente_num": 197},
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
            self.assertEqual(item["expediente"], "197/2019")

    def test_get_sentencias_by_autoridad_id_by_sentencia(self):
        """Test GET method for sentencias by autoridad_id by sentencia"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_id": 37, "sentencia": "160/2021"},
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
            self.assertEqual(item["sentencia"], "160/2021")

    def test_get_sentencias_by_autoridad_clave(self):
        """Test GET method for sentencias by autoridad_clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
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

    def test_get_sentencias_by_autoridad_clave_by_expediente(self):
        """Test GET method for sentencias by autoridad_clave by expediente"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "expediente_anio": 2019, "expediente_num": 197},
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
            self.assertEqual(item["expediente"], "197/2019")

    def test_get_sentencias_by_autoridad_clave_by_sentencia(self):
        """Test GET method for sentencias by autoridad_clave by sentencia"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias",
                headers={"X-Api-Key": config["api_key"]},
                params={"autoridad_clave": "SLT-J2-CIV", "sentencia": "160/2021"},
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
            self.assertEqual(item["sentencia"], "160/2021")

    def test_get_sentencia_by_id(self):
        """Test GET method for sentencia by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/sentencias/1",
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
