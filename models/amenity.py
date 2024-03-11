"""amenity.py

    This module contain class related to amenity

    class it defined:
        - State: country amenity

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a country amenity"""

    name = ""
