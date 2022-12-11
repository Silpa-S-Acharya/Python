
word=input("Enter the word to be checked ")
count=0
with open("text.txt",'r')as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                count=count + 1
                
print(word,":",count)
