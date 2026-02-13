t=int(input())
h={}
for i in range(t):
    b=int(input())
    for j in range(b):
        ime,score=map(str,input().split())
        if ime in h:
            h[ime]+=int(score)
        else:
            h[ime]=int(score)
l=[]
for i in h:
    l.append([h[i],i])
l.sort(reverse=True)
kolko=int(input())
for i in range(kolko):
    print(f"{l[i][1]} {l[i][0]}")