list1=[0,2,3,1,1,3,5,5,5,5,6]
for i in range (22):
    list1.append(1)
num = max(list1,key=list1.count)
print(num)