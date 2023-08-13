#!/usr/bin/python3
"""Defines the class for review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Defines a review"""

    place_id = ""
    user_id = ""
    text = ""