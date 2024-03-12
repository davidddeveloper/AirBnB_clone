"""test_review.py
    this module contains unittest test related to the class Review

"""

import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestReview.review = Review()

    def test_text(self):
        self.assertEqual(TestReview.review.text, "")
        TestReview.review.text = "Beautiful place"
        self.assertEqual(TestReview.review.text, "Beautiful place")

    def test_place_id(self):
        place = Place()
        self.assertEqual(TestReview.review.place_id, "")
        TestReview.review.place_id = place.id
        self.assertEqual(TestReview.review.place_id, place.id)

    def test_user_id(self):
        user = User()
        self.assertEqual(TestReview.review.user_id, "")
        TestReview.review.user_id = user.id
        self.assertEqual(TestReview.review.user_id, user.id)
