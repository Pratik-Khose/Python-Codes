# This is the 17CheckiftwostringsareAnagramornot.py file

first1  = input('Enter : ')
second1 = input('Enter : ')

first = first1.lower()
second = second1.lower()

firstdict = {}
seconddict = {}

for i in first:
    if i in firstdict:
        firstdict[i] += 1
    else:
        firstdict[i] = 1

for i in second:
    if i in seconddict:
        seconddict[i] += 1
    else:
        seconddict[i] = 1

if firstdict == seconddict :
    print('anagram')
else:
    print('not anagram')
