def find_missing_number(n):
    numbers=set(n)
    return [i for i in range(1,n[-1]) if i not in numbers]
listOfNumbers=[1,2,3,4,5,7,8,9,10,11,13,14,16]
print(find_missing_number(listOfNumbers))