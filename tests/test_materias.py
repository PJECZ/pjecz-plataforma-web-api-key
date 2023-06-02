"""
Unit tests for materias category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestMaterias(unittest.TestCase):
    """Tests for materias category"""

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

    def test_get_materias(self):
        """Test GET method for materias"""
        response = requests.get(f"{self.host}/v3/materias", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_materias_tipos_juicios(self):
        """Test GET method for materias_tipos_juicios"""
        response = requests.get(f"{self.host}/v3/materias_tipos_juicios", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
