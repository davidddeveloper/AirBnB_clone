"""test_place.py
    this module contains unittest test related to the class Place

"""

import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestPlace.place = Place()

    def test_name(self):
        self.assertEqual(TestPlace.place.name, "")
        TestPlace.place.name = "Alabama"
        self.assertEqual(TestPlace.place.name, "Alabama")

        # edge cases
        self.assertEqual(type(TestPlace.place.name), str)

    def test_city_id(self):
        city = City()
        self.assertEqual(TestPlace.place.city_id, "")
        TestPlace.place.city_id = city.id
        self.assertEqual(TestPlace.place.city_id, city.id)

        # edge cases
        self.assertEqual(type(TestPlace.place.city_id), str)

    def test_user_id(self):
        user = User()
        self.assertEqual(TestPlace.place.user_id, "")
        TestPlace.place.user_id = user.id
        self.assertEqual(TestPlace.place.user_id, user.id)

        # edge cases
        self.assertEqual(type(TestPlace.place.user_id), str)

    def test_amenity_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        ids = [amenity1.id, amenity2.id]
        self.assertEqual(TestPlace.place.amenity_ids, [])
        TestPlace.place.amenity_ids = ids
        self.assertEqual(TestPlace.place.amenity_ids, ids)

        # edge cases
        self.assertEqual(type(TestPlace.place.amenity_ids), list)
        self.assertNotEqual(type(TestPlace.place.amenity_ids), int)
        self.assertNotEqual(type(TestPlace.place.amenity_ids), bool)
        self.assertNotEqual(type(TestPlace.place.amenity_ids), float)
        self.assertNotEqual(type(TestPlace.place.amenity_ids), str)

    def test_description(self):
        self.assertEqual(TestPlace.place.description, "")
        TestPlace.place.description = "Beautiful scenery"
        self.assertEqual(TestPlace.place.description, "Beautiful scenery")

        # edge cases
        self.assertEqual(type(TestPlace.place.description), str)
        self.assertNotEqual(type(TestPlace.place.description), int)
        self.assertNotEqual(type(TestPlace.place.description), bool)
        self.assertNotEqual(type(TestPlace.place.description), float)
        self.assertNotEqual(type(TestPlace.place.description), list)

    def test_number_rooms(self):
        self.assertEqual(TestPlace.place.number_rooms, 0)
        TestPlace.place.number_rooms = 2
        self.assertEqual(TestPlace.place.number_rooms, 2)

        # edge cases
        self.assertEqual(type(TestPlace.place.number_rooms), int)

    def test_number_bathrooms(self):
        self.assertEqual(TestPlace.place.number_bathrooms, 0)
        TestPlace.place.number_bathrooms = 2
        self.assertEqual(TestPlace.place.number_bathrooms, 2)

        # edge cases
        self.assertEqual(type(TestPlace.place.number_bathrooms), int)

    def test_max_guest(self):
        self.assertEqual(TestPlace.place.max_guest, 0)
        TestPlace.place.max_guest = 2
        self.assertEqual(TestPlace.place.max_guest, 2)

        # edge cases
        self.assertEqual(type(TestPlace.place.max_guest), int)

    def test_price_by_night(self):
        self.assertEqual(TestPlace.place.price_by_night, 0)
        TestPlace.place.price_by_night = 2
        self.assertEqual(TestPlace.place.price_by_night, 2)

        # edge cases
        self.assertEqual(type(TestPlace.place.price_by_night), int)

    def test_latitude(self):
        self.assertEqual(TestPlace.place.latitude, 0.0)
        TestPlace.place.latitude = 2.0
        self.assertEqual(TestPlace.place.latitude, 2.0)

        # edge cases
        self.assertEqual(type(TestPlace.place.latitude), float)

    def test_longitude(self):
        self.assertEqual(TestPlace.place.longitude, 0.0)
        TestPlace.place.longitude = 2.0
        self.assertEqual(TestPlace.place.longitude, 2.0)

        # edge cases
        self.assertEqual(type(TestPlace.place.longitude), float)
