#!/usr/bin/python3
"""Module



"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        x = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[x] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as f:
            dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict, f)

    def reload(self):
        """
         deserializes the JSON file to __objects
         (only if the JSON file (__file_path)
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for ob in obj_dict.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cls_name)(**ob))

        except FileNotFoundError:
            return
