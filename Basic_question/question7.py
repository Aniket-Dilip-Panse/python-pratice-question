# Write a Python program to accept a filename from the user and print the extension of that.
filename = input('Enter the filename: ').split('.')
print(filename[-1])