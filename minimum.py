def minimum(num1,num2):
    try:
        if float(num1)<float(num2):
            print(f"{num1} is smaller than {num2}")
        elif float(num1)>float(num2):
            print(f"{num2} is smaller than {num1}")
        elif float(num1)==float(num2):
            print(f"both are equal")
    except:
        print("invalid input")
minimum("!","2")