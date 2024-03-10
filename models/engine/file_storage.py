"""file_storage.py

    This module contains classes related to file storage with json file

    classes it contained:
        - FileStorage: serializes instances to a JSON file
        and deserializes JSON file to instances

"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances

        Attributes:
            __file_path:  string - path to the JSON file
            __objects: store all objects by <class name>.id

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__class__.__objects
