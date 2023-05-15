#!/usr/bin/python3
import models
import uuid
from datetime import datetime
import file_storage

"""
this constructor defines the id attributea and some methods
"""

class BaseModel:
    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Initializes a new BaseModel.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs of attributes.
        """
        time_format = "%Y, %M, %dT, %H:%M:%S.%f"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.data():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value,
                            time_format)
                else:
                    models.storage.new(self)

    def str(self):
        """
        We have to print the initialized information information
        for printing the name of the class, we have two choices:
        1- class_name = self.__class__.__name__ and call for format(class__name__)
        2- format(type(self).__name__)
        dict: it automatically transform the initialized element into dictionary
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.dict)

    def save(self):
        """
        update the public instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()




    def to_dict(self):
        """Return a dictionary contianing all keys/values.
        The isoformat is use to print with precesion time.
        """
        
        my_dict = self.__dict__.copy()
        my_dict['class'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['update_at'] = self.updated_at.isoformat()
        return my_dict
