"""
Unit tests for distritos category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestFuncionarios(unittest.TestCase):
    """Tests for funcionarios category"""

    def setUp(self) -> None:
        """Initialize the test case"""
        # Load environment variables
        self.api_key = os.getenv("API_KEY", "")
        self.host = os.getenv("HOST", "")
        self.timeout = int(os.getenv("TIMEOUT", "20"))
        # If any of the environment variables is empty, raise an error
        if not self.api_key:
            raise ValueError("API_KEY environment variable is empty")
        if not self.host:
            raise ValueError("HOST environment variable is empty")
        if not self.timeout:
            raise ValueError("TIMEOUT environment variable is empty")
        # Return super
        return super().setUp()

    def test_get_distritos(self):
        """Test GET method for distritos"""
        response = requests.get(f"{self.host}/v3/distritos", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_distritos_by_distritos_judiciales(self):
        """Test GET method for distritos by distritos_judiciales"""
        response = requests.get(f"{self.host}/v3/distritos", headers={"X-Api-Key": self.api_key}, params={"es_distrito_judicial": 1}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        result = data["result"]
        self.assertEqual(result["total"], 14)  # Total of es_distrito_judicial is 14

    def test_get_distritos_by_distritos(self):
        """Test GET method for distritos by distritos_judiciales"""
        response = requests.get(f"{self.host}/v3/distritos", headers={"X-Api-Key": self.api_key}, params={"es_distrito": 1}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        result = data["result"]
        self.assertEqual(result["total"], 9)  # Total of es_distrito is 9

    def test_get_distritos_by_jurisdiccionales(self):
        """Test GET method for distritos by distritos_judiciales"""
        response = requests.get(f"{self.host}/v3/distritos", headers={"X-Api-Key": self.api_key}, params={"es_jurisdiccional": 1}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        result = data["result"]
        self.assertEqual(result["total"], 13)  # Total es_jurisdiccional is 13


if __name__ == "__main__":
    unittest.main()
