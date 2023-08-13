#!/usr/bin/python3
"""This module is a simple console that
handles CRUD operations on instances"""
import cmd
import json
from models.base_model import BaseModel  # Assuming BaseModel is the base class for all models
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is the class for the cmd module"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance, save it to JSON, and print the id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            cls = arg.split()[0]
            new_instance = eval(cls)()  # Assuming the class name is valid
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            cls, inst_id = args
            instance = storage.all().get(f"{cls}.{inst_id}")
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance and update JSON file"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            cls, inst_id = args
            instance = storage.all().get(f"{cls}.{inst_id}")
            if instance:
                del storage.all()[f"{cls}.{inst_id}"]
                storage.save()
            else:
                print("** no instance found **")
        except:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = arg.split()[0]
                if cls not in ["BaseModel"]:  # Add other model names if needed
                    print("** class doesn't exist **")
                    return
                print([str(obj) for key, obj in objects.items() if cls in key])
            except:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance and save changes to JSON"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            cls, inst_id, attr_name = args[:3]
            value = " ".join(args[3:])
            instance = storage.all().get(f"{cls}.{inst_id}")
            if instance:
                setattr(instance, attr_name, value)
                instance.save()
            else:
                print("** no instance found **")
        except:
            print("** class doesn't exist **")

    def emptyline(self):
        """This does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

