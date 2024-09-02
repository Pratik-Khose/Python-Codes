# This is the 15Calculatefrequencyofcharactersinastring.py file

givenstr = input("Enter the string : ")

mydict = {}

for i in givenstr:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1

print(mydict)