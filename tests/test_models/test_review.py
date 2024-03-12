"""test_review.py
    this module contains unittest test related to the class Review

"""

import unittest
from models import Review, Place, User

class TestReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestReview.review = Review()

    def test_text(self):
        self.assertEqual(TestReview.state.name, "")
        TestReview.state.name = "Beautiful place"
        self.assertEqual(TestReview.state.name, "Beautiful place")

    def test_place_id(self):
        place = Place()
        self.assertEqual(TestReview.review.place_id, "")
        TestReview.review.place_id = place.id
        self.assertEqual(TestReview.review.place_id, place.id)

    def test_user_id(self):
        user = User()
        self.assertEqual(TestReview.review.user_id, "")
        TestReview.review.user_id = place.id
        self.assertEqual(TestReview.review.user_id, place.id)
