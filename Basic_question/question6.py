# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input('enter number with comma seperated value ').split(',')
print(f'The list of values are {values}')
print(f'The tuple of values are {tuple(values)}')


#<============= method 2  =====================>
elements = input('input some comma seperated values: ')
list = elements.split(",")
tuple = tuple(list)
print(list)
print(tuple)