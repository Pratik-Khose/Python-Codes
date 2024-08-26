# This is the 25FactorsOfNumber.py file
num = int(input("Enter a number : "))
temp = 0
for i in range(2,num+1):
    if num % i == temp:
            if type(temp) == int:
                  print(f'The {i} is a factor of the {num}')
            elif type(temp) == float:
                  print(f'The {i} is not a factor of the {num}')
