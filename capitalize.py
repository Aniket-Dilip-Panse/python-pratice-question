# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

names = "aniket panse"
separate = names.split(" ")
for i in separate:
    print(i.capitalize(),end=" ")