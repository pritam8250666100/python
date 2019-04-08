lis=[2,1,3,5]
lis1=[6,4,3]
lis.extend(lis1)
for i in range(0,len(lis)):
    print(lis[i])

lis.append(lis1)
print(lis)