#  Write a  Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

first = input('Enter first name : ')
last = input('Enter last name : ')

reversefirst = first[::-1]
reverselast = last[::-1]

print(reversefirst + " " + reverselast)
