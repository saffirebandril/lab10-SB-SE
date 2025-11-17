#https://github.com/saffirebandril/lab10-SB-SE.git
#Partner 1: Saffire Bandril
#Partner 2: Sebastian Estrada

import unittest
from calculator import *
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1,2),3)
        self.assertEqual(calculator.add(-5,5),0)
        self.assertEqual(calculator.add(10,-3),7)
    def test_sub(self):
        self.assertEqual(calculator.sub(5,2),3)
        self.assertEqual(calculator.sub(10,10),0)
        self.assertEqual(calculator.sub(-3,-6),3)

    def test_multiply(self):
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(10,10), 100)
        self.assertNotEqual(mul(-10,-10), -20)

    def test_divide(self):
        self.assertEqual(div(3,9), 3)
        self.assertEqual(div(2,10), 5)
        self.assertNotEqual(div(-10,-1), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10,0)
    def test_logarithm(self):
        self.assertEqual(calculator.log(8,2),3)
        self.assertEqual(calculator.log(27,3),3)
        self.assertEqual(calculator.log(1,10),0)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10,1)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertNotEqual(hypotenuse(10,20),20)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1),1)
        self.assertEqual(square_root(9),3)
        self.assertNotEqual(square_root(2),2)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()