t=int(input())
res=0
for i in range(t):
    a,b,c,d=map(int,input().split())
    a1=(a*60)+b
    c1=(c*60)+d
    res+=c1-a1
minuti=res%60
sati=res//60
print(f"{sati} {minuti}")