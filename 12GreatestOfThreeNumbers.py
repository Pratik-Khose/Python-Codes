# This is the 12GreatestOfThreeNumbers.py file
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
num3 = float(input("Enter third number : "))
myarray = [num1,num2,num3]
# myarray.append(num1)
# myarray.append(num2)
# myarray.append(num3)

print("The greatest of three numbers is : ", max(myarray))

# by using the if statements
if num1>num2 and num1>num3:
    print(f"{num1} is greatest")
elif num2>num1 and num2>num3:
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")