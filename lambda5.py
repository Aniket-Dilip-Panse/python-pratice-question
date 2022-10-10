# Write a Python program to filter a list of integers using Lambda.
def even_odd(arr,n):
    for i in range(0,n,2):
        odd = lambda odd:i
        print(f'odd number {odd(odd)}')
    for j in range(1,n,2):
        even = lambda even:j
        print(f'even number {even(even)}')
even_odd([1,2,3,5,6,7,8,9,0],7)