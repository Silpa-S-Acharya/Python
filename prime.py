num=int(input("enter the no"))
flag=1
if num<=1:
    print("Nor prime nor composite")
else:
    for i in range(2,num):
        if num%i==0:
            flag=0
            break
    if flag==1:
        print("prime")
    else:
        print("not prime")
