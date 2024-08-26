# This is the 26FindingPrimeFactorsOfNumber.py file

n = 210
primenumbers=[]
for i in range(2,n):
    if n % i == 0:
        flag =0
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
                primenumbers.append(i)

print(primenumbers)