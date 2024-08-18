# This is the 18PalindromeNumber.py file


num = int(input('enter the number : '))
temp = num
reverse = 0
while temp>0:
    remainder = temp % 10
    reverse = (reverse * 10)+remainder
    temp = temp // 10
if num == reverse:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")