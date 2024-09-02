# This is the 08CheckifthegivenstringisPalindromeornot.py file


givenstr = input('Enter the string : ')

temp = givenstr[::-1]

if givenstr == temp:
    print('yes it is a palindrome')
else:
    print('no it is not a palindrome')