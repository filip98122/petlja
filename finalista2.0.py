a=int(input())
b=int(input())
c=int(input())
d=int(input())
e1=""
e2=""
l=[]
if a>b:
    l.append([a,"A"])
if b>a:
    l.append([b,"B"])
if c>d:
    l.append([c,"C"])
if d>c:
    l.append([d,"D"])
l.sort()
print(l[0][1])