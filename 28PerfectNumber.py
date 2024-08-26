# This is the 28PerfectNumber.py file

n = 28
sum = 0

for i in range(1,n):
    if n % i ==0:
        sum += i

if sum == n:
    print('perfect')
else:
    print('not perfect')



lower = int(input('Enter the lower limit : '))
upper = int(input('Enter the upper limit : '))
numbers = []

for n in range(lower, upper + 1):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        numbers.append(n)

print("Perfect numbers in the range:", numbers)