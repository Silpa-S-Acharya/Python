rows = int(input("Enter number of rows eg:(N=4): "))
step = int(input("Enter  step number eg:(Step=1) "))

for i in range(1,rows+1,step):
    for j in range(1,i+1,step):
        print(i*j, end=" ")
    
    print("\n")
