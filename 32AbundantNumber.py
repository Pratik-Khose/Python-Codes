# This is the 32AbundantNumber.py file
n = 100
numbers = []
for i in range(1,n):
    if n%i==0:
        numbers.append(i)
print(numbers)
    
match = sum(numbers)
print(match)
if match > n:
    print(f'so {match} is greater than {n} , so this is abandunt number')
else:
    print(f'so {match} is less than {n} , so this is not an abandunt number')
