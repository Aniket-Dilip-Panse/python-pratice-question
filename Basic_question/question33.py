# Write a Python program to add two objects if both objects are an integer type.
def int_object_check(object1,object2):
    if  (isinstance(object1, int) and isinstance(object2, int)):
       return object1 + object2
    return "Inputs must be integers!"
print(int_object_check(3,3))