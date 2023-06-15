"""
Unit tests for usuarios category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestUsuarios(unittest.TestCase):
    """Tests for usuarios category"""

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

    def test_get_bitacoras(self):
        """Test GET method for bitacoras"""
        response = requests.get(f"{self.host}/v3/bitacoras", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_bitacoras_with_modulo_clave(self):
        """Test GET method for bitacoras with modulo_clave USUARIOS"""
        response = requests.get(f"{self.host}/v3/bitacoras", params={"modulo_clave": "USUARIOS"}, headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_entradas_salidas(self):
        """Test GET method for entradas_salidas"""
        response = requests.get(f"{self.host}/v3/entradas_salidas", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_modulos(self):
        """Test GET method for modulos"""
        response = requests.get(f"{self.host}/v3/modulos", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_permisos(self):
        """Test GET method for permisos"""
        response = requests.get(f"{self.host}/v3/permisos", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_roles(self):
        """Test GET method for roles"""
        response = requests.get(f"{self.host}/v3/roles", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_usuarios(self):
        """Test GET method for usuarios"""
        response = requests.get(f"{self.host}/v3/usuarios", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_usuarios_roles(self):
        """Test GET method for usuarios_roles"""
        response = requests.get(f"{self.host}/v3/usuarios_roles", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
