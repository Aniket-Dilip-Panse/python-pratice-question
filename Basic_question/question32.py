#  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
def test_number5(num1,num2):
    if num1 == num2 or ( num1 + num2 == 5 or num1 - num2 == 5):
        return True
    else:
        return False
print(test_number5(2,2))