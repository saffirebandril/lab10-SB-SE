#https://github.com/saffirebandril/lab10-SB-SE.git
#Partner 1: Saffire Bandril
#Partner 2: Sebastian Estrada

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertNotEqual(mul(2, 3), 5)
        self.assertNotEqual(mul(2, 3), 7)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 2), 1)
        self.assertNotEqual(div(2, 3), 1)
        self.assertNotEqual(div(2, 3), 3)
    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(ValueError, logarithm, 0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertNotEqual(hypotenuse(3, 5), 1)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(ValueError, square_root, -4)
        self.assertEqual(square_root(9), 3)
        self.assertNotEqual(square_root(16), 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()