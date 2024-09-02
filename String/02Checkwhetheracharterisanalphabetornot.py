# This is the 02Checkwhetheracharterisanalphabetornot.py file

ch = 'A'

if ('a'<= ch <= 'z') or ('A'<= ch <= 'Z'):
    print(f'{ch} is Alphabet')
else:
    print(f'{ch} is not Alphabet')




def alpha_not(chr):
    if chr.isalpha():
        print(f'{chr} is alphabet')
    else:
        print(f'{chr} is not alphabet')


chr = input('enter a chr: ')
alpha_not(chr)