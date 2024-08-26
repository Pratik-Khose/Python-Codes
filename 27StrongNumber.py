# This is the 27StrongNumber.py file
num = int(input('Enter the number : '))
temp = num
sum = 0
f = [0]*10
f[0]=0
f[1]=1

for i in range(2,10):
    f[i]=f[i-1]*i

while (temp):
   r = temp % 10
   sum = sum + f[r]
   temp = temp //10

if (sum == num):
    print('This is a strong number')
else:
    print('This is not a strong number')