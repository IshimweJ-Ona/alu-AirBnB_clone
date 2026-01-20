#!/usr/bin/python3
""""Command interpreter for the AirBnB clone project."""

import cmd
from models import storage
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for System."""

    prompt= "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program with Ctrl-D (EOF)"""
        print()  # Add a new line foe clean output
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class and prints its id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print(" class doesn't exist **")
            return
        instance = classes[arg]()
        storage.save()
        print(instance.id)

    def do_show(self, arg):
        """Print instance representation"""
        args = arg.split()
        if len(args) == 0:
            print("** class name  missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id is missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id is missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Print all string instances"""
        all_objs = storage.all()
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            result = [str(obj) for k, obj in all_objs.items()
                      if k.startswith(arg + ".")]
        else:
            result = [str(obj) for k, obj in all_objs.values()]
        print(result)

    def do_update(self, arg):
        """Update an instance by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** clas doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id is missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        
        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]

        # Cast value correct type if possible
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            else:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    attr_value = attr_value.strip('"')
        except Exception:
            pass

        # Do not update protected attributes
        if attr_name in ("id", "created_at", "updated_at"):
            return
        
        setattr(obj, attr_name, attr_value)
        storage.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()