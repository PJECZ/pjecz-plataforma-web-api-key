"""
Unit tests for audiencias category
"""
import unittest

import requests

from tests.load_env import config


class TestAudiencias(unittest.TestCase):
    """Tests for audiencias category"""

    def test_get_audiencias(self):
        """Test GET method for audiencias"""
        response = requests.get(
            f"{config['host']}/v3/audiencias",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
