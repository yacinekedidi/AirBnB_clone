#!/usr/bin/python3
"""Unittest for class FileStorage([..])
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


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

    def test_save(self):
        """ test save """

        b = BaseModel()
        f = FileStorage()
        f.new(b)
        f.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """ test relaod """

        b = BaseModel()
        f = FileStorage()
        f.new(b)
        f.save()
        d = f.all()
        f.reload()
        self.assertEqual(d, f.all())

if __name__ == '__main__':
    unittest.main()
