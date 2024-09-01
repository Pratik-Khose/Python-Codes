# This is the 02FindSmallestElement.py file

a = [1,5,64,54,346,46,4,64,34,54,64,6,46,54,354,3,]

b = a[0]

for i in range(len(a)):
    if a[i] < b:
        b = a[i]

print(b)
