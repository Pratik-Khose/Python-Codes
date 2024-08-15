# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

#accept a string A from user
A = input("Enter a string of comma-separated numbers:")

#convert A into list
list_A = list(map(str, A.split(',')))
print(list_A)
#convert A into tuple
tuple_A = tuple(map(str, A.split(',')))
print(tuple_A)
