#!/usr/bin/python3
""" This module is a class for city"""


from models import BaseModel
import models


class City(BaseModel):
    """ This is the class City which inherits from BaseModel"""
    state_id = ""
    name = ""
