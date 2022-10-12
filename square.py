# we have to find the square of number between 2 to 5 which is present in list.Do not repeat the number.
def square(vlaue):
    actual_list = set(vlaue)
    for element in actual_list:
        if (element>=2 and element<=5):
            print(element * element)
        else:
            continue
square([1,23,4,5,2,2,4,2,4,52,1,1,24,3,34,3,2414,2,1,25,1,42,125,42,25,2])