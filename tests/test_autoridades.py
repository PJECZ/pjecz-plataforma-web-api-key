"""
Unit tests for autoridades
"""

import unittest

import requests

from tests.load_env import config


class TestAutoridades(unittest.TestCase):
    """Tests for autoridades"""

    def test_get_autoridades(self):
        """Test GET method for autoridades"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades",
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
            self.assertEqual("clave" in item, True)
            self.assertEqual("descripcion" in item, True)
            self.assertEqual("descripcion_corta" in item, True)

    def test_get_autoridades_by_es_cemasc(self):
        """Test GET method for autoridades by es_cemasc"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_cemasc": 1},
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
            self.assertEqual(item["es_cemasc"], 1)

    def test_get_autoridades_by_es_defensoria(self):
        """Test GET method for autoridades by es_defensoria"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_defensoria": 1},
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
            self.assertEqual(item["es_defensoria"], 1)

    def test_get_autoridades_by_es_jurisdiccional(self):
        """Test GET method for autoridades by es_jurisdiccional"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_jurisdiccional": 1},
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
            self.assertEqual(item["es_jurisdiccional"], 1)

    def test_get_autoridades_by_es_notaria(self):
        """Test GET method for autoridades by es_notaria"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_notaria": 1},
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
            self.assertEqual(item["es_notaria"], 1)

    def test_get_autoridades_by_es_organo_especializado(self):
        """Test GET method for autoridades by es_organo_especializado"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_organo_especializado": 1},
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
            self.assertEqual(item["es_organo_especializado"], 1)

    def test_get_autoridad_by_clave(self):
        """Test GET method for autoridad by clave"""
        try:
            response = requests.get(
                url=f"{config['api_base_url']}/autoridades/slt-j1-civ",
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
