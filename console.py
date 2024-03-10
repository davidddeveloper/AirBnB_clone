"""console.py

    contains the entry point of the command interpreter
    the command interpreter will be used to manipulate the file storage

    class it contained
        HBNBCommand: entry point of the command interpreter

"""

import cmd
import BaseModel

class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "
    def postloop(self):
        print()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, class_name):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id

        Args:
            class_name: name of the class to create an instance from

        """

        if !isinstance(class_name, object):
            print("** class doesn't exist **")
        elif class_name != "":
            instance = class_name()
            instance.save()
            print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, class_name, object_id):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            class_name: name of the class to create an instance from
            object_id: the id of the instance

        """
        if !isinstance(class_name, object):
            print("** class doesn't exist **")
        elif class_name != "" and object_id != "":
            print
        else:
            print("** class name missing **")

    def do_destroy(self, class_name, object_id):
        # implement
        pass

    def do_all(self, class_name):
        # implement
        pass

    def do_update(self, class_name, object_id, attr_name, value):
        # implement
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
