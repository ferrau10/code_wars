import unittest
import kyu05_rot13.main as main

class KataRot13(unittest.TestCase): 
    
    def test_rot13(self):
        text = "Test"
        expected = "Grfg"
        actual = main.rot13(text)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()