#!/usr/bin/python3
"""
Module that defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all AirBnB objects."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance."""
        from models import storage  # local import to avoid circular import
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at timestamp and save to storage."""
        from models import storage  # local import
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
