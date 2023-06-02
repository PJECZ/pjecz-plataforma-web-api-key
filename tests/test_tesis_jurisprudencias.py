"""
Unit tests for tesis_jurisprudencias category
"""
import os
import unittest

from dotenv import load_dotenv
import requests

load_dotenv()


class TestTesisJurisprudencias(unittest.TestCase):
    """Tests for tesis_jurisprudencias category"""

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

    def test_get_epocas(self):
        """Test GET method for epocas"""
        response = requests.get(f"{self.host}/v3/epocas", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_tesis_jurisprudencias(self):
        """Test GET method for tesis_jurisprudencias"""
        response = requests.get(f"{self.host}/v3/tesis_jurisprudencias", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
