# This is the 06Countthenumberofvowels.py file

tofind = input('Enter the string : ')

temp = str(tofind)
count = 0

for i in temp:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1

if count == 0:
    print('No vowels found')
else:
    print(f'{count} no of vowels are present')