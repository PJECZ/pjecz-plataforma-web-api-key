"""
Unit tests for the archivo category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestArchivo(unittest.TestCase):
    """Tests for the archivo category"""

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

    def test_get_arc_documentos(self):
        """Test GET method for arc_documentos"""
        response = requests.get(
            f"{self.host}/v3/arc_documentos",
            headers={"X-Api-Key": self.api_key},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_arc_documentos_with_distrito_clave(self):
        """Test GET method for arc_documentos with distrito_clave"""
        response = requests.get(
            f"{self.host}/v3/arc_documentos",
            headers={"X-Api-Key": self.api_key},
            params={"distrito_clave": "dslt"},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_arc_documentos_with_ubicacion(self):
        """Test GET method for arc_documentos with ubicacion"""
        response = requests.get(
            f"{self.host}/v3/arc_documentos",
            headers={"X-Api-Key": self.api_key},
            params={"ubicacion": "archivo"},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_arc_juzgados_extintos(self):
        """Test GET method for arc_juzgados_extintos"""
        response = requests.get(
            f"{self.host}/v3/arc_juzgados_extintos",
            headers={"X-Api-Key": self.api_key},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_arc_remesas(self):
        """Test GET method for arc_remesas"""
        response = requests.get(
            f"{self.host}/v3/arc_remesas",
            headers={"X-Api-Key": self.api_key},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_arc_remesas_documentos(self):
        """Test GET method for arc_remesas_documentos"""
        response = requests.get(
            f"{self.host}/v3/arc_remesas_documentos",
            headers={"X-Api-Key": self.api_key},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_arc_solicitudes(self):
        """Test GET method for arc_solicitudes"""
        response = requests.get(
            f"{self.host}/v3/arc_solicitudes",
            headers={"X-Api-Key": self.api_key},
            timeout=self.timeout,
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
