"""
Unit tests for distritos category
"""

import unittest

import requests

from tests.load_env import config


class TestDistritos(unittest.TestCase):
    """Tests for distritos category"""

    def test_get_distritos(self):
        """Test GET method for distritos"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/distritos",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)

    def test_get_distritos_by_es_distrito_judicial(self):
        """Test GET method for distritos by es_distrito_judicial"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/distritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_distrito_judicial": 1},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        for item in data["items"]:
            self.assertEqual(item["es_distrito_judicial"], 1)

    def test_get_distritos_by_es_distrito(self):
        """Test GET method for distritos by es_distrito"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/distritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_distrito": 1},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        for item in data["items"]:
            self.assertEqual(item["es_distrito"], 1)

    def test_get_distritos_by_es_jurisdiccional(self):
        """Test GET method for distritos by es_jurisdiccional"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/distritos",
                headers={"X-Api-Key": config["api_key"]},
                params={"es_jurisdiccional": 1},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        for item in data["items"]:
            self.assertEqual(item["es_jurisdiccional"], 1)


if __name__ == "__main__":
    unittest.main()
