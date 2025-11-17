#https://github.com/saffirebandril/lab10-SB-SE.git
#Partner 1: Saffire Bandril
#Partner 2: Sebastian Estrada

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(5, -5),0)
        self.assertEqual(add(10,-3),7)

    def test_sub(self):
        self.assertEqual(subtract(5,2),3)
        self.assertEqual(subtract(10,10),0)
        self.assertEqual(subtract(-3,-6),3)

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
            div(0, 10)

    def test_logarithm(self):
        self.assertEqual(logarithm(10,100),0.5)
        self.assertEqual(logarithm(2,16),0.25)
        self.assertEqual(logarithm(9,3),2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10,-1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

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


# Do not touch this
if __name__ == "__main__":
    unittest.main()