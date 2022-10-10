def match(arr,n):
    for i in range(0,n):
        if arr[i]==i:
            print(f'the number {arr[i]} is at {i} position')
        else:
            continue
match([1,1,3,4,5,6,7,8,8,9],9)