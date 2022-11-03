# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
input_number = float(input('Enter number '))
difference = input_number - 17
if input_number>17:
    print(f'the double of difference is {difference*2}')
else:
    print(abs(difference))