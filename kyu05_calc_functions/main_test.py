import unittest
import kyu05_calc_functions.main as main

class KataHumanTime(unittest.TestCase): 
    
    def test_all_functions(self):
        self.assertEqual(main.seven(main.times(main.five())), 35)
        self.assertEqual(main.four(main.plus(main.nine())), 13)
        self.assertEqual(main.eight(main.minus(main.three())), 5)
        self.assertEqual(main.six(main.divided_by(main.two())), 3)

if __name__ == '__main__':
    unittest.main()