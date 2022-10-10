import random
# creating random integer
random_integer = random.randrange(1,7)
print(random_integer)

# creating 10 random integer and storing in list
random_number_list = []
for numbers in range(1,11):
    value = random.randrange(20,70)
    random_number_list.append(value)
print(random_number_list)
