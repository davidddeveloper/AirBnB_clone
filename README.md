# AirBnB_clone
![Illustration of the Airbnb Clone Project](https://github.com/davidddeveloper/AirBnB_clone/assets/142942999/2cf1af4b-d999-4151-9d99-62fbc0e3ebfb)
The airbnb clone is a complete copy of the actual AirBnb Web application. The copy is composed by
  - A Command Interpreter
  - A website
  - A database
  - Api

## Command Interpreter
Is a command line (shell) interface for interact with the web application file storage system. Such as creating new objects, update and destroy objects.

The console or command interpreter does the following
  - create data model
  - manage objects. (create, update, destroy etc)
  - serialization and deserialization of objects to JSON file.

The console will ensentially enables us to manipulate the storage system abstractly.
  ### Execution of console
The shell works like this in interactive mode:

    $ ./console.py
    (hbnb) help
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    
    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $

But also in non-interactive mode: (like the Shell project in C)

    $ echo "help" | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
