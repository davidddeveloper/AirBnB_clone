#!/usr/bin/env python3
"""console.py

    contains the entry point of the command interpreter
    the command interpreter will be used to manipulate the file storage

    class it contained
        HBNBCommand: entry point of the command interpreter

"""

import re
import cmd
from models import storage
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User

class_names = [
        "BaseModel", "User", "City", "State", "Place", "Amenity", "Review"
]


def check(arg):
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

    if cls_name not in class_names:
        print("** class doesn't exist **")
        return

    return [cls_name, idx]


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "

    __class_names = class_names
    classes = [BaseModel, User, State, Place, City, Amenity, Review]

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

        elif cls_name not in HBNBCommand.__class_names:
            print("** class doesn't exist **")

        else:
            for i in range(len(HBNBCommand.classes)):
                # find the class to create an instance from
                # I'm doing this so I don't end up with
                # bounch of if checks for every class
                if cls_name == HBNBCommand.classes[i].__name__:
                    # class to create instance from
                    the_class = HBNBCommand.classes[i]
                    # creates a new instance
                    new = the_class()
                    storage.new(new)
                    # saves it to the JSON file
                    storage.save()
                    # print the id
                    print(new.id)
                    break

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            - arg: arguments passed to the interpreter

        """

        output = check(arg)  # perform checks
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

        output = check(arg)  # perform checks
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

        if arg != "" and arg not in HBNBCommand.__class_names:
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

        output = check(arg)  # perform checks
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
            storage.save()

        except KeyError:
            print("** no instance found **")

    def onecmd(self, s):
        """partially overwritting onecmd so we will be able to
            do the following in the console:

            User.all()  ------>  all User
            User.show("123456689")  ------>  show User 123456789
            User.destroy("123456789")  ----->  destroy User 123456789
            User.update("12345", "name", "John")  ----> update 1234 name John

        and also to perfrom User.count()

        """

        # to catch User.all() or simlar
        pattern_one = r'([A-Z][a-zA-z]*).([a-z]*)\(\)'
        if re.match(pattern_one, s):
            # ex: extract all and User from User.all()
            model, command = s.split(".")
            command = command[0:-2]  # exclude brackes

            actual_command = f"{command} {model}"  # ex: all User

            if command == "count":  # counts of all objects
                print(len(storage.all()))
                return None
            return cmd.Cmd.onecmd(self, actual_command)

        # to catch user.all("abcd") or similar
        pattern_two = r'([A-Z][a-zA-z]*)\.(\w[a-z]*)(\(("|\')\w([A-z]'
        pattern_two = pattern_two + r'|[0-9]|-)*("|\')((,\s*("|\')\w([A-z]'
        pattern_two = pattern_two + r'|[0-9]|-)*("|\'))|(,\s*\{.*\}))*\))'

        if re.match(pattern_two, s):
            # ex: extract all and User from User.all("12345")
            model, command = s.split(".")

            # ex: extract "1234" from all("1234")
            matches = re.finditer(r'("|\')(\w|[-])*("|\')', command)
            args = [m.group(0)[1:-1] for m in matches]  # get the arguments
            command, _ = command.split("(")  # extract word excluding brackets

            idx = args[0]
            actual_command = f"{command} {model}"

            # update using dictionary
            try:
                # extract dictionary
                pattern = re.compile(r'\{.*\}')
                dictionary_str = pattern.search(s).group()
                dictionary = eval(dictionary_str)

            except IndexError:
                dictionary = None

            except Exception:
                dictionary = None

            if command == "update" and dictionary is None:
                try:
                    attr_name = args[1]
                    actual_command = f"{command} {model} {idx} {attr_name}"
                except IndexError:
                    return cmd.Cmd.onecmd(self, actual_command)

                try:
                    attr_name = args[1]
                    attr_value = args[2]
                    actual_command = f"{command} {model} {idx} {attr_name}"
                    actual_command = actual_command + f" {attr_value}"
                except IndexError:
                    return cmd.Cmd.onecmd(self, actual_command)

            elif command == "update" and dictionary is not None:
                try:
                    # recreate the objects changing the key
                    # BaseModel.id to just id
                    all_objs = {}
                    objects_keys = list(storage.all().keys())
                    objects_values = list(storage.all().values())
                    for i in range(len(objects_keys)):
                        all_objs[
                                objects_keys[i].split(".")[1]
                        ] = objects_values[i]

                    instance = all_objs[idx]
                except KeyError:
                    return None

                if instance:
                    for key, value in dictionary.items():
                        setattr(instance, key, value)

                    instance.save()
                    return None

            else:
                actual_command = actual_command + f" {idx}"

            return cmd.Cmd.onecmd(self, actual_command)

        return cmd.Cmd.onecmd(self, s)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
