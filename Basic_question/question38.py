# Write a Python program to check whether a file exists.
# <================= METHOD 1 ====================>
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('matching.py'))

# <================== METHOD 2 =====================>
import os.path
print(os.path.exists('main.txt'))
print(os.path.exists('question20.py'))  #searching for file outside the folder not inside the folder
