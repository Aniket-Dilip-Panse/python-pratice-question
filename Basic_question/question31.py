# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sum_check(num1,num2):
    sum = num1 + num2
    if sum >=15 and sum <=20 :
        return 20
    else:
        return sum
print(sum_check(112, 13))