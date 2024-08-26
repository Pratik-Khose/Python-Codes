# This is the 21FibonacciSeriesUptoNthTerm.py file

num = 15
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b


num = 15
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()