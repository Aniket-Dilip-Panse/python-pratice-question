# Write a Python program to square and cube every number in a given list of integers using Lambda.
def square_cube(arr,n):
    for i in range(0,n):
        square = lambda x : x**2
        cube = lambda y : y*y*y
        print(f'square of number {square(arr)}')
        print(f'cube of number {square(arr)}')
square_cube([1,2,3,4,5,6,7,8,9],7)
