# This is the 03FindSmallestAndLargestElement.py file

a = [5,54,546,4684,54,35,546,4,5135,6545,43,44,35,4,595,1,7,687,5,54,68,7,687,6]

min = a[0]
max = a[0]

for i in range(len(a)):
    if a[i] < min:
        min = a[i]
    if a[i] > max:
        max = a[i]

print(min)
print(max)