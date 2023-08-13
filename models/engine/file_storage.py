#!/usr/bin/python3
import json
import sys
from models.base_model import BaseModel


class FileStorage:
    """ This class serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    __classes = ["BaseModel"]

    def all(self):
        """ This method returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ This method sets in __objects the obj with key
            <obj class name>.id """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ This method serializes __objects to the
            JSON file (path: __file_path) """
        _dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as json_file:
            json.dump(_dict, json_file)

    def reload(self):
        """ Deserializes the JSON file to objects """

        try:
            with open(self.__file_path, "r") as json_file:
                obj_dict = json.load(json_file)
                for key, value in obj_dict.items():
                    obj_instance = BaseModel(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
