b=int(input())
l=[]
for i in range(b):l.append(int(input()))
l.sort()
s=int(input())
#prvo brute force
for i in range(s):
    a=int(input())
    res=0
    for j in range(b):
        if a<l[j]:
            res+=1
    print(res)