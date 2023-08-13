#!/usr/bin/python3
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This class serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    __classes = {
                 "BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review
                }

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
                    cls = key.split(".")[0]
                    obj_instance = FileStorage.__classes.get(cls)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
