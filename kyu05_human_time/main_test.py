import unittest
import kyu05_human_time.main as main

class KataFindUniq(unittest.TestCase): 
    
    def test_make_readable_zero(self):
        seconds = 0
        expected = "00:00:00"
        actual = main.make_readable(seconds)
        self.assertEqual(actual, expected)

    def test_make_readable_overflow(self):
        seconds = 359999
        expected = "99:59:59"
        actual = main.make_readable(seconds)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()