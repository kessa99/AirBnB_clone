#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    constructeur
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strftime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        We have to print the initialized information information
        for printing the name of the class, we have two choices:
        1- class_name = self.__class__.__name__
        and caller format(class__name__)
        2- format(type(self).__name__)
        dict: it automatically transform
        the initialized element into dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """
        update the public instance attribute
        models.storage.save()
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary contianing all keys/values.
        The isoformat is use to print with precesion time.
        """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['update_at'] = self.updated_at.isoformat()
        return my_dict
