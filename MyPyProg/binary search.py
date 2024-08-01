l1=[1,2,3,4,5,6,7,8,9,10]
flag=0
l=0
h=len(l1)-1
m=(l+h)//2
print(l1)
n=int(input("Enter number to find="))
while(h>l and l!=m):
    if(l1[m]==n):
        flag=1
        break
    else:
        if(n>l1[m]):
            l=m
            m=(l+h)//2+1
        else:
            h=m
            m=(l+h)//2+1
    
    print("value of l,m,h:",l,m,h)
if(flag==1):
    print("Found!")
else:
    print("Not found!")
