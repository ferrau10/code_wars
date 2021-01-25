import unittest
import kyu05_moving_zeros.main as main

class KataMovingZeros(unittest.TestCase): 
    
    def test_move_zeros(self):
        self.assertEqual(main.move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
        self.assertEqual(main.move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(main.move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(main.move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])

if __name__ == '__main__':
    unittest.main()