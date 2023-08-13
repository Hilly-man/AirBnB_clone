#!/usr/bin/python3
""" This module is a class for Review"""


from models import BaseModel
import models


class Review(BaseModel):
    """ This is the class Review which inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
