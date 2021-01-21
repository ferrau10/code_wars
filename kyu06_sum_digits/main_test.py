import unittest
import kyu06_sum_digits.main as main

class KataSumDigits(unittest.TestCase): 
    
    def test_digital_root(self):
        digit = 16  
        expected = 7
        actual = main.digital_root(digit)
        self.assertEqual(actual, expected)
    
    def test_digital_root_two(self):
        digit = 942  
        expected = 6
        actual = main.digital_root(digit)
        self.assertEqual(actual, expected)

    def test_digital_root_three(self):
        digit = 493193 
        expected = 2
        actual = main.digital_root(digit)
        self.assertEqual(actual, expected)

   

if __name__ == '__main__':
    unittest.main()