import unittest
import kyu06_unique_number.main as main

class KataFindUniq(unittest.TestCase): 
    
    def test_find_uniq(self):
        numbers = [ 1, 1, 1, 2, 1, 1 ]
        expected = 2
        actual = main.find_uniq(numbers)
        self.assertEqual(actual, expected)
    
    def test_find_uniq_2(self):
        numbers = [ 0, 0, 0.55, 0, 0 ]
        expected = 0.55
        actual = main.find_uniq(numbers)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()