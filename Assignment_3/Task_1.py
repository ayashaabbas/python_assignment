#Defines a function named factorial that takes a number as an argument 
# and calculates its factorial using a loop or recursion.

#Using Recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
num = int(input("Enter a number :"))
value=fact(num)

print("The factorial of {} is {}".format(num, value))
