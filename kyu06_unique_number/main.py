#from the code wars challenge: https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i + 1]:
            continue 
        
        if i == 0:
            if arr[i+1] == arr[i + 2]:
                return arr[i]
        
        if i == len(arr):
            return arr[i]

        return arr[i + 1]
