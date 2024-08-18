# This is the 14PrimeNumber.py file

number = int(input('Enter the number : '))

flag = 0

for i in range (2,number):
    if number % i == 0:
        flag = 1
        break
if flag == 1:
    print('Number is not prime ')
elif (number == 1) or (number==0):
    print('This is not a prime number nor a composite number')
elif number < 0:
    print('Please enter a positive number')
else:
    print('Number is prime ')