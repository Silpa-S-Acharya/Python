lis=[]
a=[]
n=int(input("enter the limit: "))
print("Enter the list elements\n")
for i in range(0,n):
    print(i+1)
    elm = input()
    lis.append(elm)
print("The entered list is: ",lis)
for i in range(0,n):
    for j in lis[i]:
        c=lis.count("a")
print("Count ",c)
