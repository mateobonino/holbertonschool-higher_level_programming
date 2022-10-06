import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Base().id, 1)

    def test_2(self):
        self.assertEqual(Base().id, 2)

    def test_3(self):
        self.assertEqual(Base(59).id, 59)

    def test_4(self):
        self.assertEqual(Base().to_json_string([]), '[]')
