lis=[]
a=[]
n=int(input("enter the limit: "))
print("Enter the list elements\n")
for i in range(0,n):
    elm = int(input())
    lis.append(elm)
print("The entered list is: ",lis)
for i in lis:
    if i>100:
        a.append(i)
print("Values greater than 100 ",a)
    

    
        
       

    

