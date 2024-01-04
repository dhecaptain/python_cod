
def compute_hcf(x,y,z):
    small=min(x,y,z)
    for i in range(1,small+1):
        if (x%i==0 and y%i==0 and z%i==0):
            hcf=i
            return hcf

num1=int(input("enter the first number to compute "))
num2=int(input("enter the second number to compute "))
mum3=int(input("enter the third number to compute "))

print(f"the hcf of {num1} and {num2} and {mum3} is",compute_hcf(num1,num2,mum3))
