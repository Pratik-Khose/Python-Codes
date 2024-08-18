# This is the 13LeapYearOrNot.py file
num = int(input('Enter the year : '))


if (num% 4 ==0) or (num%100==0 or num%400==0):
    print('The year is leap')
else:
    print('The year is not leap')