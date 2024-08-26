# This is the 31HarshadNumber.py file

# n = 21 True becoz 2+1=3 and 21 is also divisible by three

n = 21
p=n
l = []
sum1 = 0
while(n>0):
    m = n % 10
    l.append(m)
    n=n//10
sum1 = sum(l)
if p % sum1 ==0:
    print('Number is Harshad number')
else:
    print('the number is not')
