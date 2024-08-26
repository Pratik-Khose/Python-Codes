# This is the 19ArmstrongNumber.py file
n = 15
temp = n
sum = 0

while temp >0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp //= 10

if sum == n:
    print("True")
else:
    print( "False")