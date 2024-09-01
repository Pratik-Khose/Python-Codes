# This is the 04FindSecondSmallestElement.py file


a = [64, 34, 25, 12, 22, 11,11, 90]

# b = a[0]

# for i in range(len(a)):
#     if a[i] > b:
#         b = a[i]

# print(b)
# print(a)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
    
print(a)

b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
