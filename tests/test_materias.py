"""
Unit tests for materias category
"""

import unittest

import requests

from tests.load_env import config


class TestMaterias(unittest.TestCase):
    """Tests for materias category"""

    def test_get_materias(self):
        """Test GET method for materias"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/materias",
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
