"""user.py
    This module contains classes and methods related to user creation

    classes it contain:
        - User: for user creation

"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
