def maximum(a,b): 
    if float(a)>float(b):
        print(f"{a} is bigger than {b}")
    elif float(a)<float(b):
        print(f"{b} is bigger than {a}")
    elif float(a)==float(b):
        print(f"both are equal")
    else:
        print("invalid input")
maximum(10,2)