# Write a Python program to display your details like name, age, address in three different lines.
def person_details(name,age,address):
    return f"your name is {name} \nyour age is {age} \nyour adress is {address}"
print(person_details('aniket', 21, 'kalyan'))


# <=============== METHOD 2 ========================>
def person_details():
    name = input('enter your name ')
    age = int(input('enter your age '))
    address = input('enter your address ')
    print(f"your name is {name} \nyour age is {age} \nyour adress is {address}")
person_details()
