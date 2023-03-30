"""
  - __init__.py
"""
import unittest
import task.gaussian_elimination_task

def square(number):
    """ :return: the square of the input number """
    return number * number

class SquareTest(unittest.TestCase):
    def test_square_positive_number(self):
        """
        Make sure your square function handles positive numbers
        """
        self.assertEqual(4, square(2))
        self.assertEqual(9, square(3))
        self.assertEqual(1, square(1))
        self.assertEqual(0, square(0))

    def test_square_negative_number(self):
        """
        Make sure your square function handles negative numbers
        """
        self.assertEqual(1, square(-1))
        self.assertEqual(4, square(-2))

    def test_square_not_a_number(self):
        with self.assertRaises(TypeError):
            square("not a number")

    def test_faulty(self):
        self.assertEqual(1, square(-1))


if __name__ == "__main__":
    # You can run this file using:   python unittest_example.py
    unittest.main()