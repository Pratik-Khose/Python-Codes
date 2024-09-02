# This is the 01Checkwhetheracharterisavowelorconsonant.py file

character = 'A'
lowerchar = character.lower()

if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u') or (lowerchar == 'a' or lowerchar == 'e' or lowerchar == 'i' or lowerchar == 'o' or lowerchar == 'u'):
    print(f'{character} is a vowel')
else:
    print('the character is not a vowel')