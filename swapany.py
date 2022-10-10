# method 1 swap by providing position in parameter
def swapany(arr , pos1 , pos2):
    arr[pos1] , arr[pos2] = arr[pos2] , arr[pos1]
    return arr
print(swapany([1,2,3,45,5,2,4,5,6,32,4,32,4,2,4,5,3,555,3,22,3,5,3,2,4],7,10))


# Python3 program to swap elements
# at given positions
# Swap function
def swapPositions(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)
    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)
    return list
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))