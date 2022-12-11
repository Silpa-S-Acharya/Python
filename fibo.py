a=int(input("enter the 1st no in the series"))
b=int(input("enter the 2nd no in the series"))
n=int(input("enter the no: of terms needed"))
print(a,b, end=" ")
while n-2:
    c=a+b
    a=b
    b=c
    print(c, end=" ")
    n=n-1
    
