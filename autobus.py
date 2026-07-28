a=int(input())
res=0
kazna="OK"
maxi=0
for i in range(a):
    iz,ul=map(int,input().split())
    res-=iz
    res+=ul
    maxi=max(res,maxi)
    if res>45:
        kazna="PRETRPAN"
print(maxi)
print(kazna)