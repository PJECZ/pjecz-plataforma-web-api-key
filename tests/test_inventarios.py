"""
Unit tests for inventarios category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestInventarios(unittest.TestCase):
    """Tests for inventarios category"""

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

    def test_get_inv_categorias(self):
        """Test GET method for inv_categorias"""
        response = requests.get(f"{self.host}/v3/inv_categorias", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_inv_componentes(self):
        """Test GET method for inv_componentes"""
        response = requests.get(f"{self.host}/v3/inv_componentes", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_inv_custodias(self):
        """Test GET method for inv_custodias"""
        response = requests.get(f"{self.host}/v3/inv_custodias", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_inv_equipos(self):
        """Test GET method for inv_equipos"""
        response = requests.get(f"{self.host}/v3/inv_equipos", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_inv_marcas(self):
        """Test GET method for inv_marcas"""
        response = requests.get(f"{self.host}/v3/inv_marcas", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_inv_modelos(self):
        """Test GET method for inv_modelos"""
        response = requests.get(f"{self.host}/v3/inv_modelos", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_inv_redes(self):
        """Test GET method for inv_redes"""
        response = requests.get(f"{self.host}/v3/inv_redes", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
