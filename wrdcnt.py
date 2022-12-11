def word_count(str):
    count=dict()
    words=str.split()
    for w in words:
        if w in count:
            count[w]+=1
        else:
            count[w]=1
    print(count)
a=input("Enter the string ")
word_count(a)
