#!/usr/bin/python3
"""console.py

    contains the entry point of the command interpreter
    the command interpreter will be used to manipulate the file storage

    class it contained
        HBNBCommand: entry point of the command interpreter

"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program

        """
        return True

    # command interpreter

    def do_create(self, cls_name):
        """creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        Args:
            - cls_name: name of the class to create a new instance from
        """

        if cls_name == "":
            print("** class name missing **")

        elif cls_name != "BaseModel":
            print("** class doesn't exist **")

        else: # cls_name is not empty and is an actual class
            # creates a new instance
            new = BaseModel()
            storage.new(new)
            # saves it to the JSON file
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            - arg: arguments passed to the interpreter

        """
        args = arg.split()
        if arg == "":
            print("** class name missing **")
            return

        if len(args) == 1:
            cls_name = args[0]
            print("** instance id missing **")
            return

        if len(args) > 1:
            cls_name = args[0]
            idx = args[1]

        if cls_name == "":
            print("** class name missing **")
            return

        if cls_name != "BaseModel":
            print("** class doesn't exist **")
            return

        try:
            instance = storage.all()[f'{cls_name}.{idx}']
            print(instance)

        except KeyError:
            print("** no instance found **")

    def do_destroy(self, BaseModel, idx):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
