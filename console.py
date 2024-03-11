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

    # reusable function
    @classmethod
    def check(cls, arg):
        """perfroms checks for do_show, do_destroy and do_all

        Args:
            - arg: the string to perform check on

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

        return [cls_name, idx]

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

        else:  # cls_name is not empty and is an actual class
            # creates a new instance
            new = BaseModel()
            storage.new(new)
            # saves it to the JSON file
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            - arg: arguments passed to the interpreter

        """

        output = HBNBCommand.check(arg)  # perform checks
        if output is not None:  # get the class name and id
            cls_name, idx = output
        else:
            return

        try:
            instance = storage.all()[f'{cls_name}.{idx}']
            print(instance)

        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""

        output = HBNBCommand.check(arg)  # perform checks
        if output is not None:  # get the class name and id
            cls_name, idx = output
        else:
            return

        try:
            del storage.all()[f'{cls_name}.{idx}']
            storage.save()

        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name

        Args:
           - arg: command line args passed to interpreter

        """

        if arg != "" and arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            objects = storage.all().values()
            print([f'{str(obj)}' for obj in objects])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)

        Arg:
            - arg: command line args passed to interpreter

        """

        output = HBNBCommand.check(arg)  # perform checks
        if output is not None:  # get the class name and id
            cls_name, idx = output
        else:
            return

        args = arg.split()
        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        try:
            instance = storage.all()[f'{cls_name}.{idx}']
            setattr(instance, attr_name, attr_value)
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
