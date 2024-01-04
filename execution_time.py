from time import time 
start=time()
word="Artificial Intelligence"
text=word.split()
a=" "
for i in text:
    a=a+str(i[0]).upper()
print(a)
end=time()
execution_time=end-start
print(f"execution time is {execution_time}")