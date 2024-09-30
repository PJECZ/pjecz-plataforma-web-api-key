"""
Unit tests for peritos
"""

import unittest

import requests

from tests.load_env import config


class TestPeritos(unittest.TestCase):
    """Tests for peritos category"""

    def test_get_peritos(self):
        """Test GET method for peritos"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
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
            self.assertEqual("perito_tipo_id" in item, True)
            self.assertEqual("perito_tipo_nombre" in item, True)
            self.assertEqual("nombre" in item, True)

    def test_get_peritos_by_tipo_de_perito_id(self):
        """Test GET method for peritos by tipo de perito"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"perito_tipo_id": 15},
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
            self.assertEqual(item["perito_tipo_id"], 15)

    def test_get_peritos_by_nombre(self):
        """Test GET method for peritos by nombre"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"nombre": "JUAN"},
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
            self.assertIn("JUAN", item["nombre"])

    def test_get_peritos_by_distrito_id(self):
        """Test GET method for peritos by distrito_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
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

    def test_get_peritos_by_distrito_id_by_tipo_de_perito(self):
        """Test GET method for peritos by distrito_id by perito_tipo_id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6, "perito_tipo_id": 15},
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
            self.assertEqual(item["perito_tipo_id"], 15)

    def test_get_peritos_by_distrito_id_by_nombre(self):
        """Test GET method for peritos by distrito_id 6 by nombre JUAN"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_id": 6, "nombre": "JUAN"},
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
            self.assertIn("JUAN", item["nombre"])

    def test_get_peritos_by_distrito_clave(self):
        """Test GET method for peritos by distrito_clave DTRC"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
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

    def test_get_peritos_by_distrito_clave_by_tipo_de_perito(self):
        """Test GET method for peritos by distrito_clave DTRC by tipo de perito 15 DACTILOSCOPIA"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC", "perito_tipo_id": 15},
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
            self.assertEqual(item["perito_tipo_id"], 15)

    def test_get_peritos_by_distrito_clave_by_nombre(self):
        """Test GET method for peritos by distrito_clave DTRC by nombre JUAN"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"distrito_clave": "DTRC", "nombre": "JUAN"},
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
            self.assertIn("JUAN", item["nombre"])

    def test_get_perito_by_id(self):
        """Test GET method for perito by id"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/peritos/1",
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
