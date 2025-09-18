#!/usr/bin/python3
"""
FileStorage engine for serializing and deserializing instances to/from a JSON file.
"""

import json
import os


class FileStorage:
    """Serializes instances to JSON and deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists."""
        if not os.path.exists(self.__file_path):
            return

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value.get("__class__")
                    cls = self._get_class(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except (json.JSONDecodeError, FileNotFoundError):
            self.__objects = {}

    def _get_class(self, name):
        """Return class by name from available models."""
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
        except ImportError:
            return None

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes.get(name)
