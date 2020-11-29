import unittest
import MathOperations


class TestMathOperations(unittest.TestCase):

    def test_add_function(self):
        pass
        # TODO: Write here unitTest

    def test_multiply_function(self):
        self.assertEqual(0, MathOperations.multiply(10, 0), "Not equal!")
        self.assertEqual(0, MathOperations.multiply(0, 10), "Not equal!")
        self.assertEqual(6, MathOperations.multiply(2, 3), "Not equal!")

    def test_equal_function(self):
        pass
        # TODO: Write here unitTest

    def test_sub_function(self):
        pass
        # TODO: Write here unitTest

    def test_absolute_function(self):
        pass
        # TODO: Write here unitTest


if __name__ == '__main__':
    unittest.main()



