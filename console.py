#!/usr/bin/python3
"""
AirBnB command interpreter.
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
    """Command interpreter for the AirBnB clone project."""

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
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D / Ctrl+Z)."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of a given class, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__classes:
            print("** class doesn't exist **")
            return
        obj = self.__classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
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
        print(obj_dict[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id, then save the change."""
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
        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """Show all string representations of instances, optionally filtered by class."""
        obj_dict = storage.all()
        obj_list = []

        if not arg:
            obj_list = [str(obj) for obj in obj_dict.values()]
        elif arg in self.__classes:
            obj_list = [str(obj) for k, obj in obj_dict.items() if k.startswith(arg + ".")]
        else:
            print("** class doesn't exist **")
            return

        print(obj_list)

    def do_update(self, arg):
        """Update an instance by adding or updating an attribute."""
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

        if attr_name in ["id", "created_at", "updated_at"]:
            return

        # Cast value to proper type
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                attr_value = attr_value.strip('"')

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
