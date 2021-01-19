#from the code wars challenge: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

def tickets(people):
    clerk = []
    for i in people:
        clerk.append(i)
        
        if i == 25:
            continue
        
        elif i == 50:
            if 25 in clerk:
                clerk.remove(25)
                continue
        
        elif i == 100: 
            if all(x in clerk for x in [25, 50]) == True:
                clerk.remove(25)
                clerk.remove(50)   
                continue
            elif clerk.count(25) >= 3: 
                for _ in range(3):
                    clerk.remove(25)
                continue

        return 'NO'
    
    return 'YES'



        
