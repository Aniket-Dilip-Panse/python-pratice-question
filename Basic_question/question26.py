# Write a Python program to concatenate all elements in a list into a string and return it.

# <===================== TEST CODE =================>
list = ['aniket','dilip','panse']
string = "".join(list)
print(string)


# <================ METHOD 2 ONLY FOR STRING ===================>
def list_join(ListElement):
    string = "".join(ListElement)
    return string
print(list_join(['aniket','panse']))


#  <==================== METHOD 3 POSSIBLE FOR INTEGER ALSO ====================>
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
print(concatenate_list_data([1, 5, 12, 2]))