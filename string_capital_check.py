# How would you check if each word in a string begins with a capital letter?
name = input("enter your name ")
capital_check = name.istitle()
if capital_check is True:
    print(f'{name} is capital ')
else:
    print(f'{name} is not capital')