# method 1
list1 = [1,2,3,4,5,6]
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)

# method 2
def  interchange(arr):
   arr[0],arr[-1] = arr[-1],arr[0]
   return  arr
print(interchange([1,2,3,4,5,6]))

# method 3 the star method *all the portion not including start and end
def swapList(list):
    start, *middle, end = list
    list = [end, *middle, start]
    return list
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# method 4 temp variable
def interchange(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return  arr
print(interchange([1,2,3,4,5]))