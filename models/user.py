#!/usr/bin/python3
"""Defines the class for class"""
from models.base_model import BaseModel

class User(BaseModel):
    """Defines a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""