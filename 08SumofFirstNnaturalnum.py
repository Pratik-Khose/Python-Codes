Number = int(input('The number till which you want sum : '))

sum = 0
for i in range(1, Number + 1):
    sum = sum + i
print("Sum of first", Number, "natural numbers is", sum)
