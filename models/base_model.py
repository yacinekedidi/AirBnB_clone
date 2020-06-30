#!/usr/bin/python3
"""Module



"""
import uuid
import datetime
import models


class BaseModel:
    """
    parent of all our classes
    """
    def __init__(self, *args, **kwargs):
        """init instance"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            tf = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == "created_at":
                    self.__dict__[k] = datetime.datetime.strptime(v,  tf)
                elif k == "updated_at":
                    self.__dict__[k] = datetime.datetime.strptime(v, tf)
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """returns obj as string repr"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
         updates the public instance attribute
         updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dict = {"__class__": self.__class__.__name__}
        dict.update(self.__dict__)
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
