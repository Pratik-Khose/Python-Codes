# This is the 08SortArray.py file
# Bubble sort program ahead:-

def sorting(myarr):

    for i in range(len(myarr)):
        for j in range(len(myarr)-1-i):
            if myarr[j] > myarr[j+1]:
                myarr[j], myarr[j+1] = myarr[j+1], myarr[j]
    return myarr

# sorting(myarr)
a = [9,5,6,7,8,1,3,4,6,2,5]

numbers = sorting(a)
print(numbers)