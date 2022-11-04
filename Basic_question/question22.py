# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
def input_string(str):
    copies = int(input('enter number of copies of string: '))
    if len(str)>2:
        return str[0:2]*copies
    else:
        return str
print(input_string('abcdef'))