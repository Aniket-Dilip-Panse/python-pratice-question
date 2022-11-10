# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
# distance formula = under root of (x1-x2)^2 + (y1 - y2)^2
# <====================== METHOD 1 =========================>
import math
point1 = [4,0]
point2 = [6,6]
distance = math.sqrt( ((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2) )
print(distance)

# <====================== METHOD 2 ============================>
x1 = float(input('enter the value of x1: '))
y1 = float(input('enter the value of y1: '))
x2 = float(input('enter the value of x2: '))
y2 = float(input('enter the value of y2: '))
distance_formula = ((x1-x2)**2 + (y1-y2)**2)**0.5
print(round(distance_formula,2))