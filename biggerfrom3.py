print("Enter the 3 no:s")
a=int(input("\nEnter the 1st no: "))
b=int(input("\nEnter the 2nd no: "))
c=int(input("\nEnter the 3rd no: "))
if a>b and a>c:
    print(a,"\t is biggest")
elif b>a and b>c:
    print(b,"\t is biggest")
else:
    print(c,"\t is biggest")
