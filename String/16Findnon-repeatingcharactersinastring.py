# This is the 16Findnon-repeatingcharactersinastring.py file

givenstr = input('Enter the string: ')

mydict = {}

# Count the frequency of each character in the string
for i in givenstr:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1

# Print the non-repeating characters
# non_repeating_chars = [char for char in mydict if mydict[char] == 1]
print(mydict)

bhar = []


for char in mydict:
    if mydict[char] == 1:
        bhar.append(char)

reasult = ''.join(bhar)    

print(reasult)
# print("Non-repeating characters: ", non_repeating_chars)
