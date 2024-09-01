# # This is the 01FindLargestElement.py file

# a = [1,15,13,7,65,8,14,11,98,33,26,52,11]

# a.sort()
# max_ele =a[0]
# print(a[::2])
# for i in range(len(a)):
#     if a[i] > max_ele:
#         max_ele= a[i]

# print(max_ele)



# a=[]
# for i in range(0,100):
#     if i > 0:
#         a.append(i)
# print(a)
# print(a[:50:-1] and a[:50:1])
# print(max(a))






























mygiven = [1,5,9,3,5,74,56,1,60,4,56,7,8,4,50,4,6,47,20,7,89,7]

mymax = mygiven[0]

for i in range(len(mygiven)):
    if mygiven[i] > mymax:
        mymax = mygiven[i]

print(mymax)

mygiven.sort()
print(mygiven)

print(max(mygiven))