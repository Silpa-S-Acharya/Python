a=int(input("enter the no:"))
s=0
t=a
while(a>0):
    r=a%10
    n=r*r*r
    s=s+n
    a=a//10
print(s)
if t==s:
    print("Armstrong")
else:
    print("Not armstrong")
