def fibonacci_none_recursive(n): 
    
    a = 0
    b =1
    c= a + b
    if n == 0:
        return 0
    elif(n == 1 or n == 2):
        return 1
        
    else: 
        while (n>=0):
            
            a=b
            b=c
            c= a+b
    return (c)
           
print(fibonacci_none_recursive(10))        