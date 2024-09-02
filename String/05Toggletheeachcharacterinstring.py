# This is the 05Toggletheeachcharacterinstring.py file

givenstr = "PrAtIk Khose"

genestr = str()

for i in givenstr:
    if i.isupper():
        i = i.lower()
        genestr += i

    else:
        i = i.upper()
        genestr += i

print(genestr)
