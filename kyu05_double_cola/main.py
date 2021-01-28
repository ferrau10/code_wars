#from the code wars challenge: https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/
def who_is_next(names, r):
    #step 1: find interval n:
    n = 0

    small = 1
    while r >= small:    
        small = small + len(names)*2**n
        n+=1 

    n = n-1
    small = small - len(names)*2**(n)  
    
    #step 2: find the place in interval 
    if n == 0:
        step = r 
    else: 
        place = r - small + 1
        step = place/(2**n)
    
    #step 3 find the right name:
    for i in range(len(names)):
        if step <= i + 1:
            return names[i]

