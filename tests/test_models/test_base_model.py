#!/usr/bin/python3
"""Unittest for class BaseModel([..])
"""
import unittest
from models.base_model import BaseModel
import models
import os


class TestBaseModel(unittest.TestCase):
    """class"""

    def test_args(self):
        """test without args"""

        b = BaseModel()
        b1 = BaseModel()
        b2 = BaseModel(id='Betty')
        b3 = BaseModel(name="Ali")
        b4 = BaseModel(**b1.to_dict())
        self.assertRaises(AttributeError)
        self.assertEqual(b2.id, "Betty")
        self.assertTrue(hasattr(b2, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertFalse(hasattr(b2, "created_at"))
        self.assertFalse(b1.id == b2.id)
        self.assertNotEqual(b.id, b1.id)
        self.assertEqual(b1.id, b4.id)
        self.assertEqual(b1.created_at, b4.created_at)
        self.assertEqual(b1.updated_at, b4.updated_at)

    def test_str(self):
        """ test print """

        b1 = BaseModel()
        b2 = BaseModel(id='Betty')
        s = "[{}] ({}) {}".format("BaseModel", b1.id, b1.__dict__)
        self.assertEqual(print(s), print(b1))
        self.assertIsInstance(b1.__str__(), str)

        s = "[{}] ({}) {}".format("BaseModel", b2.id, b2.__dict__)
        self.assertEqual(print(s), print(b2))

    def test_dict(self):
        """ to_dict """

        b1 = BaseModel()
        d = {"__class__": b1.__class__.__name__}
        d.update(b1.__dict__)
        d["created_at"] = b1.created_at.isoformat()
        d["updated_at"] = b1.updated_at.isoformat()
        self.assertEqual(print(d), print(b1.to_dict()))
        self.assertIsInstance(b1.to_dict(), dict)

    def test_file(self):
        """ test storege """

        self.assertTrue(os.path.exists("file.json"))
        x = 0
        b1 = BaseModel()
        b1.save()
        models.storage.reload()
        d = models.storage.all()
        for k in d.keys():
            if b1.id in k:
                x = 1

        self.assertEqual(x, 1)

if __name__ == '__main__':
    unittest.main()
