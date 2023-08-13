#!/usr/bin/python3
""" This module is a simple console that handles EOF and exit"""
import sys
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	"""This is the class for the cmd module"""
	
	prompt = "(hbnb) "

	def do_quit(self, line):
		"""This method exits the cmd line"""
		return True
	
	def do_EOF(self, line):
		"""This method exits the console"""
		return True

	def do_create(self, line):
		"""This method creates a new instance of BaseModel"""
		if not line:
			print("** class name missing **")
			return False
		try:
			cls = line.split()[0]
			new_instance = eval(cls)()
			new_instance.save()
			print(new_instance.id)
		except NameError:
			print("** class doesn't exist **")

	def do_show(self, line):
		"""This prints the str format of the created object"""

		if not line:
			print("** class name missing **")
			return False
		args = line.split()
		cls = args[0]
		for key, value in storage.all().items():
			flag = False
			if cls in key:
				flag = True
		if flag is False:
			print("** class doesn't exist **")
			return False
		
		if len(args) < 2:
			print("** instance id missing **")
			return False
		inst_id = args[1]
		storage.reload()
		try:
			instance = storage.all()[f"{cls}.{inst_id}"]
			if instance:
				print(instance)
		except KeyError:
			print("** no instance found **")

	def do_destroy(self, line):
		""" This method deletes an instance of BaseModel"""
		if not line:
			print('** class name missing **')
			return False

		args = line.split()
		cls = args[0]
		flag = False
		for key, value in storage.all().items():
			if cls in key:
				flag = True
		if flag is False:
			print("** class doesn't exist **")
			return False
		if len(args) < 2:
			print("** instance id missing **")
			return False
		inst_id = args[1]
		storage.reload()
		try:
			instance = storage.all().get(f"{cls}.{inst_id}")
			if instance:
				del storage.all()[f"{cls}.{inst_id}"]
				storage.save()
			else:
				print("** no instance found **")
		except KeyError:
			print("** class doesn't exist **")
	
	def postcmd(self, stop, line):
		if not sys.stdin.isatty():
			print()
		return stop

	def emptyline(self):
		"""This does nothing"""
		pass

if __name__ == '__main__':
	HBNBCommand().cmdloop()
