"""city.py

    This module contain class related to city

    class it defined:
        - State: country city

"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a country City"""

    state_id = ""
    name = ""
