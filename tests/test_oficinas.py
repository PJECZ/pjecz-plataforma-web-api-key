"""
Unit tests for oficinas category
"""

import unittest

import requests

from tests.load_env import config


class TestOficinas(unittest.TestCase):
    """Tests for oficinas category"""

    def test_get_domicilios(self):
        """Test GET method for domicilios"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/domicilios",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)

    def test_get_oficinas(self):
        """Test GET method for oficinas"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/oficinas",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.ConnectionError as error:
            self.fail(f"Connection error: {error}")
        except requests.exceptions.Timeout as error:
            self.fail(f"Timeout error: {error}")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
