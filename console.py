#!/usr/bin/python3
""""Command interpreter for the AirBnB clone project."""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()