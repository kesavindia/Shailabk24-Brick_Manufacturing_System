# test_calculator.py
import pdb
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Set up any initial conditions needed for the tests
        self.calculator = Calculator()
    pdb.set_trace()
    def tearDown(self):
        # Clean up after the tests
        pass

    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
