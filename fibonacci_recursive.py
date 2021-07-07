#FINISHED
def fibonacci(n):
    """This is a recursive function
    to find the factorial of an integer"""
    if (n<0 or n>30):
        return ("incorrect input")     
    elif n==0:
        return 0
    elif(n==1 or n==2):
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))





    

