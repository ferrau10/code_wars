#from the code wars challenge: https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    num = seconds

    num, seconds =  divmod(num, 60)
    if seconds > 59:
        seconds = 59
        num = num + seconds - 59 
    
    num, minutes =  divmod(num, 60)
    if minutes > 59:
        minutes = 59
        num = num + minutes - 59 

    
    return "%02d:%02d:%02d" % (num, minutes, seconds)