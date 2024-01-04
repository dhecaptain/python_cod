def mean(list1):
    
    median=sum(list1)/len(list1)
    print(f'the mean is {median}')
    
def median(list1):
    list1.sort()
    list1=int(list1)
    if (list1)%2 == 0:
        m1=list1[len(list1)//2]
        m2=list1[len(list1)//2-1]
        median=(m1+m2)/2
    else:
        median=list1[len(list1)//2]
    print(f'the median of {list1} is: {median}')

def mode(list1):
    frequency={}
    for i in list1 :
        frequency.setdefault(i,0)
        frequency[i]+=1
    frequent=max(frequency.values())
    for i,j in frequency.items():
        if j==frequent:
            print(f'the mode is {i}')
            
            
    
list1=[12,16,20,12,30,25,23,24,20]
mean(list1)
mode(list1)
median(list1)
