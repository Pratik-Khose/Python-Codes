# This is the 09SunofNnaturalnum.py file
Number1 = int(input('The Number you want to sum : '))
Number2 = int(input('The Number you want to sum : '))

sum = 0

for num in range(Number1,Number2+1):
    sum = sum + num
print(sum)