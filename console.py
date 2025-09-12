#!/usr/bin/python3
"""
This module contains the entry point of the AirBnB command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB Clone project.
    Provides a command-line interface to manage AirBnB objects.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF (Ctrl+D).
        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        Prevents repeating the last command.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

