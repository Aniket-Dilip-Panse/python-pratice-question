# Write a Python program to count the number 4 in a given list
def count_4(list):
    count = 0
    for element in list:
        if element == 4:
            count = count + 1
    return count
print(count_4([1,2,3,4,5,6,7,8,9,4,1,2,3,4,6,7,8,9,4]))