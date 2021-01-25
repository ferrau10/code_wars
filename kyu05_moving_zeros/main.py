#from the code wars challenge: https://www.codewars.com/kata/52597aa56021e91c93000cb0/

def move_zeros(array):
    number = sum((x == 0 and x is not False) for x in array)
    array = [i for i in array if i != 0 or i is False]
    for i in range(number):
      array.append(number * 0)
    return array