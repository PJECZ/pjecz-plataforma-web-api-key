"""
Unit tests for materias category
"""

import unittest

import requests

from tests.load_env import config


class TestMateriasTiposJuicios(unittest.TestCase):
    """Tests for materias-tipos juicios category"""

    def test_get_materias_tipos_juicios(self):
        """Test GET method for materias_tipos_juicios"""
        try:
            response = requests.get(
                f"{config['api_base_url']}/materias_tipos_juicios",
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
