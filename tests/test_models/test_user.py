"""Tests for user.py

"""

import unittest
import uuid
import json
from models.user import User


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        TestUser.model1 = User()
        TestUser.model2 = User()

    @classmethod
    def tearDownClass(self):
        pass

    def test__init__with_kwargs(self):
        new_model = User(**(TestUser.model1.to_dict()))

        self.assertEqual(new_model.__dict__, TestUser.model1.__dict__)

    def test__init__with_empty_kwargs(self):
        new_model = User({})

        self.assertIsNotNone(new_model.id)
        self.assertIsNotNone(new_model.created_at)
        self.assertIsNotNone(new_model.updated_at)

    def test__init_with_args(self):
        # we are not going to use args in our model creating
        # but we still have to test it

        new_model = User(
                "2017-09-28T21:03:54.052298",
                "2017-09-28T21:03:54.052302",
                "56d43177-cc5f-4d6c-a0c1-e167f8c27337", {})

        self.assertNotEqual(new_model.created_at.isoformat(), "2017-09-28T21:03:54.052298")
        self.assertNotEqual(new_model.updated_at.isoformat(), "2017-09-28T21:03:54.052302")
        self.assertNotEqual(new_model.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")

    def test_id_type(self):
        self.assertEqual(isinstance(TestUser.model1.id, str), True)

    def test_id_unique(self):
        self.assertEqual(TestUser.model1.id == TestUser.model2.id, False)

    def test_created_at(self):
        model1datecreated = TestUser.model1.created_at
        model2datecreated = TestUser.model2.created_at

        self.assertEqual(model1datecreated == model2datecreated, False, "Should be false")
        self.assertEqual(model1datecreated.hour == model2datecreated.hour, True, "should be true")

    def test_updated_at(self):
        self.assertEqual(TestUser.model2.updated_at, TestUser.model2.created_at)
        # update model
        TestUser.model2.id = str(uuid.uuid4())
        self.assertNotEqual(TestUser.model2.updated_at, None, "should be true")

    def test__str__(self):
        result = str(TestUser.model1)
        expected_result = f"[{TestUser.model1.__class__.__name__}] ({TestUser.model1.id}) {TestUser.model1.__dict__}"
        self.assertEqual(result, expected_result)

    def test_save(self):
        current_updated_date = TestUser.model1.updated_at

        # updated model
        TestUser.model1.id = str(uuid.uuid4())
        TestUser.model1.save()  # updated updated_at

        self.assertNotEqual(current_updated_date, TestUser.model1.updated_at)

    def test_to_dict(self):
        model3 = User()
        expected_output = model3.__dict__['created_at']
        expected_output = expected_output.isoformat()

        self.assertEqual(model3.to_dict()['created_at'], expected_output)
