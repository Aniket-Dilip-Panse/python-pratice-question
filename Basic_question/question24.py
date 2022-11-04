# Write a Python program to check whether a specified value is contained in a group of values.
def value_check(number):
    list = [1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
    if number in list:
        return "number is present inside list"
    else:
        return "number is not present inside list"
print(value_check(5))

# <========================== METHOD 2 ===========================>
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False