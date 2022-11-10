''''a=30
b=30
x=15
y=25
if b>a:
    c=a+b
    if x<y:
        z=x*3
    else:
        z=x-y
elif a==b:
    c=a+b
    if x>y:
        z=x*2
    elif x==y:
        z=y*2
    else:
        z=x+y
else:
    c=a+b
    if x>y:
        z=y*5
    else:
        z=x*10
print(c)
print(z)'''''
#program2
'''mark=60
if mark<10:
    z=mark*2
elif mark<30:
    z=mark*3
elif mark<50:
    z=mark*4
else:
    z=mark*10
print(z)'''
a=[5,10,15]
l=[]
for x in a:
    d=x*2
    print(d)
    l.append(d)
print(l)
s=[1,2,5,8,12,15]
b=[]
for i in s:
    if i%2!=0:
        b.append(i)
print(b)

