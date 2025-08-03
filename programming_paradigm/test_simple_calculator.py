import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
    def test_subtraction(self):
        """""Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-20, 15), -35)
    
    def test_multiplication(self)
        """""Test the multiplication method."""
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-10, 2), -20)
        
    def test_division(self):
        """""Test the division method."""
        self.assertEqual(self.calc.divide(50, 5), 10)
        self.assertEqual(self.calc.divide(-100, 10), -10)
        
    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 10), 0)

    def test_division_by_zero_denominator(self):
        self.assertIsNone(self.calc.divide(10, 0))
    

if __name__ == '__main__':
    unittest.main()
    
