# from the code wars challenge: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    while len(str(n)) > 1:
        c = 0 
        for i in range(len(str(n))):
            c = c + int(str(n)[i]) 
        n = c 
    
    return n 

