#from the code wars challenge: https://www.codewars.com/kata/53368a47e38700bd8300030d

names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
s = ''

for i in range(len(names)):

    if len(names) == 1:
        s = s + names[0]['name']


    elif len(names) == 2:
        s = s + names.pop(0)['name'] + ' & '

    else:
        s = s + names.pop(0)['name'] + ', '

print(s)