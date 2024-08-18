# This is the 17ReverseOfNumber.py file

num = int(input('enter number : '))

reverse = 0

while num >0:
    remainder = num % 10
    reverse = (reverse *10) +remainder
    num = num //10

print(reverse)