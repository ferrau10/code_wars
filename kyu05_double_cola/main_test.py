import unittest
import kyu05_double_cola.main as main

class KataDoubleCola(unittest.TestCase): 
    
    def test_who_is_next(self):
        names= ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        r =52
        expected = "Penny"
        actual = main.who_is_next(names, r)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()