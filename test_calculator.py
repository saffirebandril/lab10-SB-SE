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

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
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

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

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