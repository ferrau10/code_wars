import unittest
import kyu06_pig_latin.main as main

class KataFindUniq(unittest.TestCase): 
    
    def test_pig_it(self):
        text = 'Pig latin is cool'
        expected = 'igPay atinlay siay oolcay'
        actual = main.pig_it(text)
        self.assertEqual(actual, expected)

    def test_pig_it_punctuationn(self):
        text = 'Hello world !'
        expected = 'elloHay orldway !'
        actual = main.pig_it(text)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()