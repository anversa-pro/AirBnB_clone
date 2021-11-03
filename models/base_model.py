#!/usr/bin/python3
"""
BASE MODEL
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    Base class definition
    """

    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Modify the stdr output with a specific format """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a Dictionary with specific attributes """
        """__dict__ returns only set attrinbutes???"""
        printDictionary =  self.__dict__.copy()
        printDictionary.update({'id': self.id, 'created_at': self.created_at.isoformat(),
                           'updated_at': self.updated_at.isoformat(), '__class__': type(self).__name__})
        return printDictionary
