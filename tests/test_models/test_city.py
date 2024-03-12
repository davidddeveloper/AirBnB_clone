"""test_city.py
    this module contains unittest test related to the class city

"""

import unittest
from models import State, City

class TestCity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestCity.city = State()

    def test_name(self):
        self.assertEqual(TestCity.city.name, "")
        TestCity.city.name = "Alabama"
        self.assertEqual(TestCity.city.name, "Alabama")

    def test_state_id(self):
        state = State()
        self.assertEqual(TestCity.city.state_id, "")
        TestCity.city.state_id = state.id
        self.assertEqual(TestCity.city.state_id, state.id)
