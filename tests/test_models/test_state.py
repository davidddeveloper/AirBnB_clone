"""test_state.py
    this module contains unittest test related to the class State

"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestState.state = State()

    def test_name(self):
        self.assertEqual(TestState.state.name, "")
        TestState.state.name = "Alabama"
        self.assertEqual(TestState.state.name, "Alabama")
