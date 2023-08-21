import cmd
import json
import os
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # Print a newline before exiting
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return

        classes = models.classes()
        if arg not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        classes = models.classes()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        key = args[0] + "." + args[1]
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        classes = models.classes()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        key = args[0] + "." + args[1]
        if key in objects:
            objects.pop(key)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        objects = models.storage.all()

        if not args:
            obj_list = [str(obj) for obj in objects.values()]
            print(obj_list)
        else:
            classes = models.classes()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return

            obj_list = [str(obj) for key, obj in objects.items() if args[0] in key]
            print(obj_list)

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        classes = models.classes()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        key = args[0] + "." + args[1]
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        obj = objects[key]
        if hasattr(obj, attr_name):
            setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
            obj.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
