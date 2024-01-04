def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return x /y
    else:
        print("cant divide by zero")

x=int(input("enter value of x: "))
y=int(input("enter value of y: "))

print(""" choose an operation
        1=add
        2=sub
        3=mul
        4=div
    
""")
choice=input("Enter your choice 1/2/3/4: ")

if choice=="1":
    print(f"x+y=",add(x,y))
elif choice=="2":
    print(f"x-y=",sub(x,y))
elif choice=="3":
    print(f"x*y=",mul(x,y))
elif choice=="4":
    print(f"x/y=",div(x,y))
else:
    print("INVALID choice!!!")
    