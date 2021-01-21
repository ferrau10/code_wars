import unittest
import kyu06_encoder.main as main

class KataEncoder(unittest.TestCase): 
    
    def test_duplicate_encode_unique(self):
        text = "din"  
        expected = "((("
        actual = main.duplicate_encode(text)
        self.assertEqual(actual, expected)

    def test_duplicate_encode_diff(self):
        text = "recede"
        expected = "()()()"
        actual = main.duplicate_encode(text)
        self.assertEqual(actual, expected)

    def test_duplicate_encode_case(self):
        text = "Success"
        expected = ")())())"
        actual = main.duplicate_encode(text)
        self.assertEqual(actual, expected)

    def test_duplicate_encode_char(self):
        text = "(( @"  
        expected = "))((" 
        actual = main.duplicate_encode(text)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()