#!/usr/bin/python3
"""Unittest for class State([..])
"""

import unittest
from models.state import State
import models
import os


class TestState(unittest.TestCase):
    """class test"""

    def test_attribute(self):
        """ test attribute  """

        u = State()
        self.assertIsInstance(u.name, str)
        self.assertTrue(issubclass(State, models.base_model.BaseModel))

    def test_args(self):
        """test without args"""

        u = State()
        u1 = State()
        u2 = State(id='Betty')
        u3 = State(name="Ali")
        u4 = State(**u1.to_dict())
        self.assertEqual(u2.id, "Betty")
        self.assertTrue(hasattr(u2, "id"))
        self.assertTrue(hasattr(u1, "created_at"))
        self.assertTrue(hasattr(u1, "updated_at"))
        self.assertFalse(hasattr(u2, "created_at"))
        self.assertFalse(u1.id == u2.id)
        self.assertNotEqual(u.id, u1.id)
        self.assertEqual(u1.id, u4.id)
        self.assertEqual(u1.created_at, u4.created_at)
        self.assertEqual(u1.updated_at, u4.updated_at)

    def test_str(self):
        """ test print """

        u1 = State()
        u2 = State(id='Betty')
        s = "[{}] ({}) {}".format("State", u1.id, u1.__dict__)
        self.assertEqual(print(s), print(u1))
        self.assertIsInstance(u1.__str__(), str)

        s = "[{}] ({}) {}".format("State", u2.id, u2.__dict__)
        self.assertEqual(print(s), print(u2))

    def test_dict(self):
        """ to_dict """

        u1 = State()
        d = {"__class__": u1.__class__.__name__}
        d.update(u1.__dict__)
        d["created_at"] = u1.created_at.isoformat()
        d["updated_at"] = u1.updated_at.isoformat()
        self.assertEqual(print(d), print(u1.to_dict()))
        self.assertIsInstance(u1.to_dict(), dict)

    def test_file(self):
        """ test storege """

        self.assertTrue(os.path.exists("file.json"))
        x = 0
        u1 = State()
        u1.save()
        models.storage.reload()
        d = models.storage.all()
        for k in d.keys():
            if u1.id in k:
                x = 1

        self.assertEqual(x, 1)

if __name__ == '__main__':
    unittest.main()

