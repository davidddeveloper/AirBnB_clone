"""test_amenity.py
    this module contains unittest test related to the class Amenity

"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestAmenity.amenity = Amenity

    def test_name(self):
        self.assertEqual(TestAmenity.amenity.name, "")
        TestAmenity.amenity.name = "Alabama"
        self.assertEqual(TestAmenity.amenity.name, "Alabama")
