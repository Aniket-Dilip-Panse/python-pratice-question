# Write a Python function to reverses a string if it's length is a multiple of 4.
input_string = input("Enter any sentence or paragraph ")
if len(input_string) % 4 == 0:
    print(input_string[::-1])
else:
    print(f"length of the string is not the multiple of 4 {input_string}")