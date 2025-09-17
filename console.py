#!/usr/bin/python3
"""
This module contains the entry point of the AirBnB command interpreter.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D / Ctrl+Z).
        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_help(self, arg):
        """Display help information about commands.
        Usage: help or help <command>
        """
        if arg:
            func = getattr(self, 'do_' + arg, None)
            if func:
                print(func.__doc__ or f"No detailed help for {arg}")
            else:
                print(f"No help available for {arg}")
        else:
            print("Documented commands (type help <topic>):")
            commands = [cmd for cmd in dir(self) if cmd.startswith('do_')]
            for cmd_name in commands:
                print(f" {cmd_name[3:]}")

    def do_create(self, arg):
        """
        Create a new instance of a given class, saves it,
        and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance
        based on class and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id,
        then save the change.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """
        Show all string representations of instances.
        Can filter by class name if provided.
        Usage: all or all <class_name>
        """
        obj_list = []
        obj_dict = storage.all()
        if not arg:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            if arg not in self.__classes:
                print("** class doesn't exist **")
                return
            for key, obj in obj_dict.items():
                if key.startswith(arg + "."):
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an
        attribute, then save.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = obj_dict[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except Exception:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
