list1=[]
len=int(input("How many names do you want to insert "))
for i in range(0,len):
    print("Enter the name you want to insert  ",i+1)
    fname=input()
    list1.append(fname)
    count_a=0
for names in list1:
    count_a+=names.count("a")
print("Occurrence of a in given list is ",count_a)
