"""test_state.py
    this module contains unittest test related to the class State

"""

import unittest
from models import State

class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestCity.state = State()

    def test_name(self):
        self.assertEqual(TestCity.state.name, "")
        TestCity.state.name = "Alabama"
        self.assertEqual(TestCity.state.name, "Alabama")
