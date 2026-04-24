a,b=map(str,(input().strip()).split())
a1,b1=map(str,(input().strip()).split())
a2,b2=map(str,(input().strip()).split())
l=[a,b,a1,b1,a2,b2]
l.sort()
last=False
for i in range(1,6):
    if l[i]==l[i-1]:
        if last:
            print(l[i])
            exit()
        last=True
    else:
        last=False
print("nemoguce")