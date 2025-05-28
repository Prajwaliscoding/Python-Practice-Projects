list=[1,2,4,5,4,3,6,6,90,20,20,21,1,4,5,3,2,65,5]
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)
