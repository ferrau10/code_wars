import unittest
import kyu06_missing_letter.main as main

class KataMissingLetterTests(unittest.TestCase): 
    
    def test_find_missing_letter_small(self):
        letters = ["a","b","c","d","f"] 
        expected = "e"
        actual = main.find_missing_letter(letters)
        self.assertEqual(actual, expected)
    
    def test_find_missing_letter_big(self):
        letters = ["O","Q","R","S"]
        expected = "P"
        actual = main.find_missing_letter(letters)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()