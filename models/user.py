#!/usr/bin/python3
"""
User class for AirBnB clone.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Public class inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
