#!/usr/bin/python3
"""
Defines the FileStorage class for JSON 
serialization and deserialization.
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serialization instances to a json file and 
    deserialise json file to instances.
    """

    __file_path = "file.json"
    __objects = {}  # dictionay storing all objects

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Add a new object to __objects dict
        format: <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the json file.
        Convert each object to a dictionary using to_dict().
        """
        obj_dict = {key: obj.to_dict() for key, 
                    obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f, indent=4)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists.
        If the file doesn't exist do nothing.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                # recreates objects from dictionary
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass  # if file doesn't exist
