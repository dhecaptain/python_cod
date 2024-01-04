input_list=[[10,20,30],[40,50,60],[70,80,90]]
output_list=[]
index=0

for _ in range(len(input_list[0])):
    output_list.append([])
    for input_ in input_list:
        output_list[index].append(input_[index])
    index=index+1
a,b,c=output_list[0],output_list[1],output_list[2]
print(a,b,c)