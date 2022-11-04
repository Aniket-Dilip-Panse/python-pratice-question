# Write a Python program to test whether a passed letter is a vowel or not.
def character_check(char):
    if char in 'aeiou':
        return 'The character is vowel '
    else:
        return 'The character is constonant'
print(character_check('a'))