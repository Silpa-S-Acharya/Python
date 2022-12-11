'''s=""
print(s.count("a"))'''
n=int(input("Enter the start range"))
m=int(input("Enter the end range"))
a=[]
print("Positive no:")
for i in range(-n,m):
    if i>0:
        a.append(i)
    else:
        print("negatives")
print("Positive no:")
print(a)

              
