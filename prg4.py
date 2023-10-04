"""
Write a Python function that takes a number as an input from the user and computes its
factorial with recursion
"""
def factorial(n):
    fact = 1
    while(n>0):
            fact = fact*n
            n-=1
        
    return fact

n = int(input("Enter a number: "))
print("The factorial of",n ,"is :", factorial(n))
