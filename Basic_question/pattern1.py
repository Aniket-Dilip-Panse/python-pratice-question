# solid rectangle
def SolidRectangle(row,col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            print("*",end=" ")
        print(" ")
SolidRectangle(4,5)