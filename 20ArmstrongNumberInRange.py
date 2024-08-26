# This is the 20ArmstrongNumberInRange.py file
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

for i in range(num1,num2):
    power = len(str(i))
    temp = i
    sum = 0
    while temp >0:
        digit = temp % 10
        cube = digit ** power
        sum = sum + cube
        temp //= 10

    if sum == i:
        print(f"{i} is armstrong number")
    