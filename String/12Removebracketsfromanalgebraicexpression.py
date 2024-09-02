# This is the 12Removebracketsfromanalgebraicexpression.py file

a=['[',']','{','}','(',')']
   
string = '(x+y)+[z+q]'

for i in string:
    if i not in a:
        print(i,end='')
