def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)

num=int(input("enter a number to check it's factorial: "))
print(factorial(num))