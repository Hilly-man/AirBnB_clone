#!/usr/bin/python3
import json
""" This module contains a class which is responsible for file storage """

class FileStorage():
	""" This class serializes instances to a JSON file
		and deserializes JSON file to instances
		"""

		__file_path = "file.json"
		__objects = {}

		def all(self):
			""" This method returns the dictionary __objects"""
				return self.__objects
		def new(self, obj):
			""" This method sets in __objects the obj with key <obj class name>.id"""

				self.__objects[f'{obj.__class__}.{obj.id}'] = obj.__dict__

		def save(self):
			""" This method serializes __objects to the JSON file(path: __file_path) """
				with open(self.__file_path, "w") as json_file
				for obj in self.__objects:
					json.dump(self.__objects[obj], json_file)

					
