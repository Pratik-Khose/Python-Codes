# This is the 07RemovethevowelsfromaString.py file

user = input('Enter the input : ')

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]

reasult = ""

for char in user:
    if char not in vowels:
        reasult += char


print(reasult)
