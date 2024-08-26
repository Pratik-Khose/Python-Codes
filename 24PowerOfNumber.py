# This is the 24PowerOfNumber.py file
num = int(input('Enter the number : '))

improv = num**(0.5)
# print(improv)
improv1= int(improv)
if improv == improv1:
    print(f'The number is the perfect square of {improv1}')
else:
    print(f'The number is not the perfect square of anynumber its square root is {improv}')


# if type(improv)==int:
#     print("The number is integer")
# else:
#     print('The number is decimal')