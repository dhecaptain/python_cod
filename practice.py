import time
import calendar
def prime_number():
        for num in range(10,20):
                for i in range(2,num):
                        if num%i==0:
                                j=num/i
                                print("{} equals {} * {} ".format(num,i,j))
                                break
                else:
                                print(f"{num} is a prime number")

def trial():
        for letter in "python":
                print(letter)
                if letter=='o':
                        break
localtime=time.localtime(time.time())
print(localtime)
cal=calendar.month(2023,12)
print(cal)