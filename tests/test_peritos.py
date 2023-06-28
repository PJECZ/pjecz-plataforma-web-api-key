"""
Unit tests for peritos category
"""
import unittest

import requests

from tests.load_env import config


class TestPeritos(unittest.TestCase):
    """Tests for peritos category"""

    def test_get_peritos(self):
        """Test GET method for peritos"""
        response = requests.get(
            f"{config['host']}/v3/peritos",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)

    def test_get_peritos_by_distrito_id_6(self):
        """Test GET method for peritos by distrito_id 6"""
        response = requests.get(
            f"{config['host']}/v3/peritos",
            headers={"X-Api-Key": config["api_key"]},
            params={"distrito_id": 6},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        result = data["result"]
        for item in result["items"]:
            self.assertEqual(item["distrito_id"], 6)


if __name__ == "__main__":
    unittest.main()
