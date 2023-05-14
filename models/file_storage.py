#!/usr/bin/python3
"""
- the task consists in adding methods to the FileStorage class 
of the file models/engine/file_storage.py and to link the BaseModel class

-Add the private attributes __file_path and __objects to the FileStorage class. 
The former must be a string representing the path to the JSON file in which the objects will be stored,
 while the latter is an empty dictionary that will contain all objects by class name and identifier.

 -initialize the __file_path attribute with the path to the JSON file using 
 os.path.abspath(os.path.dirname(__file__)) to get the absolute path of the current directory and the file name file.json.
"""
from models.base_model import BaseModel
import json
import os.path

class FileStorage:
    """
    This code initialization allows to define the private attribute __file_path of the current instance (self) of the class. 
    More precisely, it assigns it the value of the absolute path to the file "file.json" located in the parent directory ('..') 
    of the current directory (os.path.dirname(__file__)), which corresponds to the directory containing the current Python file.

Thus, __file_path will be used to store the serialized data in a JSON file, using this absolute path as the storage file location.
    """
    __file_path = None
    __objects = {}
    def __init__(self):
        self.__file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'file.json'))
        self.reload()
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """
        serialisation of content
        """
        with open(self.__file_path, 'W') as f:
            obj_dict = {key:obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict,f)
    
    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_id, obj_dict in obj_dict.items():
                    cls_name = obj_dict.pop('__class__', None)
                    if cls_name and cls_name in BaseModel.__subclasses__():
                        obj = BaseModel.__subclasses__()[cls_name](**obj_dict)
                        self.__objects[obj_id] = obj
        except FileNotFoundError:
            pass
