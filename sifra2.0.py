l=[]
for i in range(26):
    l.append(list(map(str,input().split())))
a="abcdefghijklmnopqrstuvwxyz"
b=int(input())
res=""
for i in range(b):
    c=input()
    res=res+l[a.find(c[0])][a.find(c[1])]
print(res)