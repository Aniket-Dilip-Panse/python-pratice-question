def nterm(n):
    count=0
    for i in range(1,n+1):
        print(i)
        count = count + i
    print(f"the sum of nth natural number is {count}")
nterm(1000)