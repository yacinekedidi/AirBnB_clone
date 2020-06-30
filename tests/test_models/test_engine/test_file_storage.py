#!/usr/bin/python3
"""Unittest for class FileStorage([..])
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """test"""

    def test_attribute(self):
        """ function all """

        f = FileStorage()
        self.assertIsInstance(f._FileStorage__objects, dict)
        self.assertIsInstance(f._FileStorage__file_path, str)

    def test_all(self):
        """ test all """

        f = FileStorage()
        d = f.all()
        self.assertIsInstance(d, dict)

    def test_new(self):
        """ test new """

        b = BaseModel()
        f = FileStorage()
        f.new(b)
        self.assertEqual(b, f.all()["BaseModel" + "." + b.id])

if __name__ == '__main__':
    unittest.main()
