#!/usr/bin/python3
import uuid
from datetime import datetime

"""
this constructor defines the id attributea and some methods
"""

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

    def str(self):
        """
        We have to print the initialized information information
        for printing the name of the class, we have two choices:
        1- class_name = self.__class__.name and call for format(class__name__)
        2- format(type(self).name)
        dict: it automatically transform the initialized element into dictionary
        """
        return "[{}] ({}) {}".format(type(self).name, self.id, self.dict)

    def save(self):
        """
        update the public instance attribute
        """
        self.created_at = datatime.now()
        self.updated_at = datetime.now()



    def to_dict(self):
        """Return a dictionary contianing all keys/values.
        The isoformat is use to print with precesion time.
        """
        
        my_dict = self.dict.copy()
        my_dict['class'] = self.__classname__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['update_at'] = self.updated_at.isoformat()
        return my_dict




