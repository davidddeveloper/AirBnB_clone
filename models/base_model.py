"""base_model.py

    This modules contains definitions of all common attributes and method
    for other classes

    classes it contained
        - BaseModel: provides the base definition for other classes

"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """provides the base/foundation for other classes
    including ids and other common attributes

    Attributes:
        - id: unique identify of the object created with uuid4
        - created_at: holds the current date the object was created
        - updated_at: assign with the current datetime when object was created
        also assign with the current datetime when the object is modify/change

    """

    objects = {}

    def __init__(self, *args, **kwargs):

        # gets the dictionary representation of all objects
        obj_dict_repr = [x.to_dict() for x in storage.all().values()]

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        if kwargs not in obj_dict_repr:
            storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        and a key __class__ with the value of the class name of the object

        """

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
