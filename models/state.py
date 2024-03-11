"""state.py

    This module contain class related to state

    class it defined:
        - State: country state

"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a country state"""

    name = ""
