# Airbnb clone - The console

## Project Description
This project is about creating an Airbnb clone.
It consist of building a command line interpreter(CLI) to manage Airbnb objects such as User, City, Place, and more

The command interpreter allow us to:
-Create new objects from storage
-Retrieve objects from storage
-Update object attributes
-Destroy objects
-Persist objects using JSON serialization

## Command interpreter description
The command interpreter works like a shell but is limited to a specific use cases for Airbnb project.
It provides an interface to manage the project's models and storage system.

Available actions include:
-**Create** new instances
-**Show** details of an instance
-**Destroy** an instance
-**Update** attributes of an instance
-**All* to list all instances
-**Count** instances of a class

-----------------

## How to start it 
Make sure you have Python 3 (version 3.8.5 installed).
Clone the repository and navigate into it like follow:

```
git clone https://github.com/<your-username>/alu-AirBnB_clone.git
cd alu-AirBnB_clone
```

Make console.py executable:
```
chmod +x console.py
```

Start the interpreter in 
-Interactive mode: ` ./console.py `

-Non-interactive mode:
``` 
echo "help" | ./console.py
```

--------------------------------------
## How to use it 
In interactive mode you get a prompt (hbnb) where you can type commands.
In non-interactive mode you can pipe commands or scripts into the interpreter.
Use **help** to list available commands or help <command> to get help about a specific one.

For example: 
Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode
```
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
```


