# This is the 06ReverseArray.py file

a = [1,1,9,7,6,4,8,2,3,5]
b = []
a.sort(reverse=True)
print(a)

for i in a:
    if i not in b:
        b.append(i)
print(b)


def sortit(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

sortit(a)

print(a)

print(a[::-1])



def sortingmy(arraes):
    start = 0
    end = len(arraes)-1

    while start < end:
        arraes[start],arraes[end] = arraes[end], arraes[start]

        start+=1
        end-=1

myarray = [1,2,3,4,5,6,7,8,9]
sortingmy(myarray)
print("Reversed array:", myarray)