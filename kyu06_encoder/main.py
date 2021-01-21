# from the code wars challenge: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    s = ''
    for i in word: 
        if word.lower().count(i.lower()) == 1: 
            s = s + '('
        else:
            s = s + ')'
    return s
    

