# This is the 10Removeallcharactersfromstringexceptalphabets.py file

givenstr = input('Enter the string : ')

temp = ''

for i in givenstr:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ( i == ' '):
        temp += i

print(temp, end= ' ')