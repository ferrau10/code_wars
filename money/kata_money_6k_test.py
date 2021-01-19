import unittest
import kata_money_6k

class KataMoneyTests(unittest.TestCase): 
    
    def test_tickets(self):
        people = [25, 25, 50]
        expected = 'YES'
        actual = kata_money_6k.tickets(people)
        self.assertEqual(actual, expected)
    
    def test_tickets_2(self):
        people = [25, 100]
        expected = 'NO'
        actual = kata_money_6k.tickets(people)
        self.assertEqual(actual, expected)

    def test_tickets_3(self):
        people = [25, 25, 50, 50, 100]
        expected = 'NO'
        actual = kata_money_6k.tickets(people)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()