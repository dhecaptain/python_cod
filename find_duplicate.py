def find_duplicate(x):
    length=len(x)
    duplicate=[]
    for i in range(length):
        n=i+1
        for a in range (n,length):
            if x[i]==x[a]and x[i] not in duplicate:
                duplicate.append(x[i])
    return duplicate
names=['david','wambua','lily','shazzy','willy','david','lily','njenga']
print(find_duplicate(names))