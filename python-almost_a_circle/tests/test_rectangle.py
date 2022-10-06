import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_2(self):
        rect2 = Rectangle(1, 2, 3)
        self.assertEqual(rect2.id, 8)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)

    def test_3(self):
        rect3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect3.id, 9)
        self.assertEqual(rect3.width, 1)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 3)
        self.assertEqual(rect3.y, 4)