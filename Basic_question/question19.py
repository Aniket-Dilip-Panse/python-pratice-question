# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def normal_string(str):
    string_copies = int(input('enter the number of copies of string you want: '))
    return str*string_copies
print(normal_string('.test'))

# <================= METHOD 2 ==================>
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result
print(larger_string('.test',5))