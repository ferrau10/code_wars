#from the code wars challenge: https://www.codewars.com/kata/5672682212c8ecf83e000050/solutions/python

def dbl_linear(n):
    u = [1]
    i = 0
    while len(u) <= n * 10:
        x = u[i]
        u.append(2 * x + 1)
        u.append(3 * x + 1)
        i += 1

    return sorted(set(u))[n] 