import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):


    def normal_list(self):
        self.assertEqual(max_integer([1, 3, 7, 11]), 11)

    def negative_expected(self):
        self.assertEqual(max_integer([-5, -15, -3, -6]), -15)

    def float_list(self):
        self.assertEqual(max_integer([10.5, 16.7, 0.5]), 16.7)

    def strings_error(self):
        self.assertEqual(max_integer(["this", "is", "a", "unittest"]), "unittest")

if __name__ == "__main__":
    unittest.main()