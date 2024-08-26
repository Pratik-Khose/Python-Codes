# This is the 15PrimeNumberInRange.py file
start = int(input('Enter the number : '))
end = int(input('Enter the number : '))
numbers=[]
numbers.append(1)

for x in range(start,end+1):
    flag = 0

    if x<2:
        continue
    elif x==2:
        numbers.append(2)
        continue
    for i in range(2,x):
        if x % i == 0:
            flag = 1 
            break
    if flag==0:
        numbers.append(x)

print(numbers)


