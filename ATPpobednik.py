t=int(input())
h={}
for i in range(t):
    ime,score=map(str,input().split())
    if ime in h:
        h[ime]+=int(score)
    else:
        h[ime]=int(score)
l=[]
for i in h:
    l.append([h[i],i])
l.sort(reverse=True)
print(f"{l[0][1]} {l[0][0]}")