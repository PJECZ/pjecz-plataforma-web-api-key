"""
Unit tests for siga category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestSiga(unittest.TestCase):
    """Tests for siga category"""

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

    def test_get_siga_salas(self):
        """Test GET method for siga_salas"""
        response = requests.get(f"{self.host}/v3/siga_salas", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_siga_grabaciones(self):
        """Test GET method for siga_grabaciones"""
        response = requests.get(f"{self.host}/v3/siga_grabaciones", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_siga_bitacoras(self):
        """Test GET method for siga_bitacoras"""
        response = requests.get(f"{self.host}/v3/siga_bitacoras", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
