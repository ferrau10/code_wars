#from the code wars challenge: https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i]) - ord(chars[i + 1]) == -1:
            continue 
        return chr(ord(chars[i]) + 1)
    