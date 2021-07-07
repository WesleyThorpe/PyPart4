
import random
         
a = random.randint(1,10)

while True:
    value = input("please provide a number between 0,10:\n")
    value = int(value)
    if value < a:
        print("guess is too low")    

    elif value > a: 
        print("guess is too high")

    else:
        print("you guessed it")
        break
    
#print("the random number was:", a)
#print("your guess was:", value)