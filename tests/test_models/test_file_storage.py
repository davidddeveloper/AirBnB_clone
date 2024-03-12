"""Tests for test_file_storage.py

"""

import unittest
import uuid
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        TestFileStorage.filename = os.path.join(
                os.path.dirname(__file__), '..', '..', 'file.json'
        )

        TestFileStorage.storage = FileStorage()
        TestFileStorage.model1 = BaseModel()

    @classmethod
    def tearDownClass(self):
        pass

    def test_file_exist(self):
        TestFileStorage.model1.name = "Model 1"
        TestFileStorage.model1.save()

        self.assertTrue(os.path.exists(TestFileStorage.filename))

    def test_file_contain_valid_data(self):
        model2 = BaseModel()
        model2.save()

        file_exists = os.path.exists(TestFileStorage.filename)
        if not file_exists:
            return

        with open(TestFileStorage.filename, 'r', encoding='utf-8') as f:
            self.assertNotEqual(f.read(), "")

            f.seek(0)
            expected_output = json.load(f)
            expected_output = expected_output[f"BaseModel.{model2.id}"]

            actual_output = model2.to_dict()

            self.assertEqual(model2.to_dict(), expected_output)

    def test_all_for_valid_data(self):
        data = TestFileStorage.storage.all()
        self.assertNotEqual(None, data)
        self.assertNotEqual([], data)
        self.assertNotEqual("", data)

    def test_all_with_valid_data(self):
        all_objs = TestFileStorage.storage.all()

        file_exists = os.path.exists(TestFileStorage.filename)
        if not file_exists:
            return

        with open(TestFileStorage.filename, 'r', encoding='utf-8') as f:
            TestFileStorage.storage.save() # save recent changes

            dictionary_from_json = json.load(f)
            all_objs_keys = list(all_objs.keys()) # list of keys
            dictionary_from_json_keys = list(dictionary_from_json.keys())

            self.assertEqual(dictionary_from_json_keys, all_objs_keys)

    def test_all_type(self):
        all_objs = TestFileStorage.storage.all()
        self.assertTrue(isinstance(all_objs, dict))

    def test_new_with_valid_args(self):
        new = BaseModel()
        new_obj_id = f'BaseModel.{new.id}'

        # check the object is added to __objects
        # were check against keys
        list_of_all_objs_keys = list(TestFileStorage.storage.all().keys())

        self.assertIn(new_obj_id, list_of_all_objs_keys)

    def test_save(self):
        new_model = BaseModel()
        new_model.name = "New model 101"
        new_model.save()

        # check the new object is save to file
        # by checking against keys
        file_exists = os.path.exists(TestFileStorage.filename)
        if not file_exists:
            return

        with open(TestFileStorage.filename, 'r', encoding='utf-8') as f:
            list_of_objs_dict_keys = list(json.load(f).keys())
            new_model_keys = f'BaseModel.{new_model.id}'

            self.assertIn(new_model_keys, list_of_objs_dict_keys)

