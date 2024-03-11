#!/usr/bin/python3
"""file_storage.py

    This module contains classes related to file storage with json file

    classes it contained:
        - FileStorage: serializes instances to a JSON file
        and deserializes JSON file to instances

"""

import json
import os


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

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Arguments:
            - obj: the instance to add to __objects

        """

        self.__class__.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id
        )] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__class__.__file_path, "w", encoding='utf-8') as f:
            # first convert obj to dictionary
            obj_dict_repr = {}
            for ids, value in self.__class__.__objects.items():
                obj_dict_repr[ids] = value.to_dict()

            json.dump(obj_dict_repr, f)

    def reload(self):
        """deserializes the JSON file to __objects
        only if the JSON file exist

        I'm doing the imports below to avoid circular imports

        """
        from models.base_model import BaseModel
        from models.user import User

        file_exist = os.path.exists(self.__class__.__file_path)

        if file_exist:
            with open(self.__class__.__file_path, "r", encoding='utf-8') as f:

                obj_dict_repr = json.load(f)

                # converts the dictionary to object
                # that can be stored in __objects
                for key, dictionary in obj_dict_repr.items():
                    cls_name = dictionary["__class__"]

                    if cls_name == "BaseModel":
                        self.__class__.__objects[key] = BaseModel(**dictionary)
                    elif cls_name == "User":
                        self.__class__.__objects[key] = User(**dictionary)
