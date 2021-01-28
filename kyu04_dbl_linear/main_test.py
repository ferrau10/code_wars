import unittest
import kyu04_dbl_linear.main as main

class KataDblLinear(unittest.TestCase): 
    
    def test_dbl_linear(self):
        expected = 22
        actual = main.dbl_linear(10)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()