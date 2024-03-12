"""test_amenity.py
    this module contains unittest test related to the class Amenity

"""

import unittest
from models import Amenity


class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestCity.amenity = Amenity

    def test_name(self):
        self.assertEqual(TestCity.amenity.name, "")
        TestCity.amenity.name = "Alabama"
        self.assertEqual(TestCity.amenity.name, "Alabama")
