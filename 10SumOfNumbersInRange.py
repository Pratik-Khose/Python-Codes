# This is the 10SumOfNumbersInRange.py file
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
sum=0
if (num1 or num2) <0:
    print("Please enter positive numbers")
elif (num1 or num2)==0:
    print("zero is not a natural number")
else:
    for i in range(num1,num2+1):
        sum += i
    print(sum)
