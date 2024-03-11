"""review.py

    This module contain class related to review

    class it defined:
        - State: country review

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a country review"""

    place_id = ""
    user_id = ""
    text = ""
