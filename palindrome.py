a=int(input("enter the no:"))
r=0
t=a
while a>0:
    rem=a%10
    r=r*10+rem
    a=a//10
print(r)
if t==r:
    print("Palindrome")
else:
    print("Not palindrome")
