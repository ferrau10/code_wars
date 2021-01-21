# from the code wars challenge: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string

def is_pangram(s):
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in s.lower():
            return False
    
    return True

