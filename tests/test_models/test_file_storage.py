"""Tests for test_file_storage.py

"""

import unittest
import uuid
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        TestBase.filename = "../../file.json"
        TestBase.storage = FileStorage()
        TestBase.model1 = BaseModel()
        TestBase.all_dictionary = TestBase.storage.all()

    @classmethod
    def tearDownClass(self):
        pass

    def test_file_exist(self):
        TestBase.model1.name = "Model 1"
        TestBase.model1.save()

        self.assertTrue(os.path.exists(TestBase.filename))

    def test_file_contain_valid_data(self):

        with open(TestBase.filename, 'r', encoding='utf-8') as f:
            self.assertNotEqual(f.read(), "")
            
            expected_output = json.load(f)
            actual_output = TestBase.model1.to_dict()
            actual_output['updated_at'] = actual_output['updated_at'].isoformat()
            actual_output['created_at'] = acutal_output['created_at'].isoformat()

            self.assertEqual(TestBase.model1.to_dict(), expected_output)

    def test_all_for_valid_data(self):
        self.assertNotEqual(None, TestBase.all_dictionary)
        self.assertNotEqual([], TestBase.all_dictionary)
        self.assertNotEqual("", TestBase.all_dictionary)

    def test_all_with_valid_data(self):
        with open(TestBase.filename, 'r', encoding='utf-8') as f:
            dictionary_from_json = json.load(f)

            self.assertEqual(dictionary_from_json, all_dictionary)

    def test_all_type(self):
        self.assertTrue(isinstance(TestBase.all_dictionary, dict))

    def test_new_with_valid_args(self):
        storage.new({"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}})
        storage.save()

    def test_save(self):
        new_model = BaseModel()
        new_model.name = "New model 101"
        new_model.save()

        with open(TestBase.filename, 'r', encoding='utf-8') as f:
            dictionary_from_json = json.load(f)

