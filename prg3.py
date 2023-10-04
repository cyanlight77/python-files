"""
Write a Python function to return nth terms of Fibonacci sequence
"""
def fib(n):
    if n<0 :
        print("Invalid Input")
    elif n==1:
        term = 0
    elif n==2:
        term = 1
    else:
        term = fib(n-1)+fib(n-2)
    return term

n = int(input("Enter the nth term: "))

print("Term",n ,"of Fibonacci sequence: ", fib(n))
        