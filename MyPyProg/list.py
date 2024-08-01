sum=0
n=0
l1=[]
n=int(input("How many number you want to enter?"))
for i in range (0,n,1):
    n2=int(input("Please enter a number"))
    sum+=n2
    l1.append(n2)
print("Average=",sum/n)
print("Max=",max(l1))
print("Min=",min(l1))
    
