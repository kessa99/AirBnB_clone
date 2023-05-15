#!/usr/bin/python3
"""This defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Signify a User.

    Attributes:
        email (str): The email address of user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
