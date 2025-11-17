import unittest
from calculator import *
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1,2),3)
        self.assertEqual(calculator.add(-5,5),0)
        self.assertEqual(calculator.add(10,-3),7)
    def test_sub(self):
        self.assertEqual(calculator.subtract(5,2),3)
        self.assertEqual(calculator.subtract(10,10),0)
        self.assertEqual(calculator.subtract(-3,-6),3)

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
        self.assertEqual(calculator.logarithm(8,2),3)
        self.assertEqual(calculator.logarithm(27,3),3)
        self.assertEqual(calculator.logarithm(1,10),0)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10,1)

    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(ValueError,logarithm, 0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertNotEqual(hypotenuse(10,20),20)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(ValueError, square_root, -1)
        self.assertEqual(square_root(1),1)
        self.assertNotEqual(square_root(2),2)


# Do not touch this
if __name__ == "__main__":
    unittest.main()