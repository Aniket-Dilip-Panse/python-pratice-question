# Write a Python program to create a histogram from a given list of integers.
histograph_list = [2,5,7,9,2,5,7]
for value in histograph_list:
    print('@'*value)


# <================= METHOD 2 ========================>
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])