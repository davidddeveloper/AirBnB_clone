#!/usr/bin/python3
"""console.py

    contains the entry point of the command interpreter
    the command interpreter will be used to manipulate the file storage

    class it contained
        HBNBCommand: entry point of the command interpreter

"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_emptyline():
        pass

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program

        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
