"""test_city.py
    this module contains unittest test related to the class city

"""

import unittest
from models.state import State
from models.city import City

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
        self.assertEqual(City.state_id, "")
        State.state_id = state.id
        self.assertEqual(State.state_id, state.id)
