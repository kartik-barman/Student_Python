l1=[5,6,1,4,10,9,8,3,2,7]
i=0
for i in range(0,10):
    for j in range(i+1,10):
        if(l1[i]>l1[j]):
            t=l1[i]
            l1[i]=l1[j]
            l1[j]=t
print(l1)
flag=0
n=int(input("Enter number to search="))
for i in range(0,10):
    if(l1[i]==n):
        flag=1
        break
if(flag==1):
    print("Found!")
else:
    print("Can not find the number")

        
    

