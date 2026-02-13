a,b=map(int,input().split())
w1,h1=map(int,input().split())
w2,h2=map(int,input().split())
a1=a
b1=b
a2=b
b2=a
res=4
if w1+w2>a1 or max(h1,h2)>b1:
    res-=1
if h2+h1>b1 or max(w1,w2)>a1:
    res-=1
if w1+w2>a2 or max(h1,h2)>b2:
    res-=1
if h2+h1>b2 or max(w1,w2)>a2:
    res-=1
print(res)