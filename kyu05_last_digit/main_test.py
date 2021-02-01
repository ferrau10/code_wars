import unittest
import kyu05_last_digit.main as main

class KataLastDigit(unittest.TestCase): 
    
    def test_last_digit(self):
        self.assertEqual(main.last_digit(4, 1), 4)
        self.assertEqual(main.last_digit(4, 2), 6)
        self.assertEqual(main.last_digit(9, 7), 9)
        self.assertEqual(main.last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

if __name__ == '__main__':
    unittest.main()