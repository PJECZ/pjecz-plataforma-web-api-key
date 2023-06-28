"""
Unit tests for abogados category
"""
import unittest

import requests

from tests.load_env import config


class TestAbogados(unittest.TestCase):
    """Tests for abogados category"""

    def test_get_abogados(self):
        """Test GET method for abogados"""
        response = requests.get(
            f"{config['host']}/v3/abogados",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
