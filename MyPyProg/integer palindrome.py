n=int(input("Enter any number="))
ncopy=n
s=0
while(ncopy!=0):
    r=ncopy%10
    s=s*10+r
    ncopy=ncopy//10
if(n==s):
    print("Palindrome")
else:
    print("Not Palindrome")
