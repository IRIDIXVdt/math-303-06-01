import unittest
# import task.gaussian_elimination_task as task
# from ...python_file.task.gaussian_elimination import upper_triangular
import gaussian_elimination_task as ge

class SquareTest(unittest.TestCase):

    def test_ge_bs(self):
        """
        Test Gaussian Elimination
        """
        input1 = [[ 1. ,-2., -1., 6.], [ 2. , 2., -1. , 1.], [-1. ,-1.,  2. , 1.]]
        output1 =  [3.0, -2.0, 1.0]
        self.assertEqual(ge.gauss(input1),output1)
        # self.assertEqual(1,2)

    def test_square_negative_number(self):
        """
        Make sure your square function handles negative numbers
        """
        self.assertEqual(1, 1*1)

if __name__ == "__main__":
    # You can run this file using:   python unittest_example.py
    unittest.main()