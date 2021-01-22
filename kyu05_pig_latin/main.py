#from the code wars challenge: https://www.codewars.com/kata/520b9d2ad5c005041100000f

import string 

def pig_it(text):
    s = ''
    for i in text.split(): 
        if i in string.punctuation:
            s = s + i
        else:
            s = s + i[1:] + i[0] + 'ay'+ ' '
            
    return ' '.join(s.split())