import unittest
import kyu06_pangram.main as main

class KataPangramTests(unittest.TestCase): 
    
    def test_is_pangram(self):
        pangram = "The quick, brown fox jumps over the lazy dog!"
        expected = True
        actual = main.is_pangram(pangram)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()