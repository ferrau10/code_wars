import unittest
import kyu06_dubstep.main as main

class KataDubstep(unittest.TestCase): 
    
    def test_song_decoder(self):
        song = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB" 
        expected = 'WE ARE THE CHAMPIONS MY FRIEND'
        actual = main.song_decoder(song)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()