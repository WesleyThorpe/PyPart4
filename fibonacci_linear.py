
#FINISHED 
def fibonacci_none_recursive(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif (n==1 or n==2):
            
            return(b)
    else:        
        for i in range(2,n):
            c = a+b
            a =b
            b=c
        return(a+b)

print (fibonacci_none_recursive(10))
    
    
   