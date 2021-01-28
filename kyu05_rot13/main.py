#from the code wars challenge: https://www.codewars.com/kata/530e15517bc88ac656000716/
from string import ascii_lowercase, ascii_uppercase

def rot13(message):

    s = ''
    for i in message:
        if i in ascii_lowercase:
            s = s + ascii_lowercase[(ascii_lowercase.index(i)+13) % 26]
        elif i in ascii_uppercase:
            s = s + ascii_uppercase[(ascii_uppercase.index(i)+13) % 26]
        else: 
            s = s + i

    return s