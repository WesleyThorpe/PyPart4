import math
def our_constraint(n):
    if (n <=0 or n >995): 
        return ("incorrect input")

    elif n==1:
        return 1

    else:
       return math.factorial(n)         
       # return our_constraint(math.factorial(n))
         #n! = n × (n−1)!

print(our_constraint (5))      