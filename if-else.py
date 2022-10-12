# Task
# Given an integer,n , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20 , print Not Weird
def even_odd(value):
        if value%2 != 0:
            print("Weird")
        elif (value%2==0 and 5>=value>=2):
            print("Not Weird")
        elif (value%2==0 and 20>=value>=6):
            print("Weird")
        elif (value%2==0 and value>20):
            print("Not Weird")
even_odd(2)