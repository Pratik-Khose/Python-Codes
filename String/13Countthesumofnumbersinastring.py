# This is the 13Countthesumofnumbersinastring.py file

givenstr = input('Enter the string : ')

temp = 0

for i in givenstr:
    if i in '0123456789':
        temp += int(i)

print(temp)