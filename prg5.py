"""
Write a Python function that takes a number as an input from the user and computes its
factorial without recursion
"""
def fact_rec(n):
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n*fact_rec(n-1)
    return fact

n = int(input("Enter a number: "))
print("The factorial of",n ,"is :", fact_rec(n))
