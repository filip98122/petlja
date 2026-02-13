sijalica = int(input())
l = list(map(int, input().split()))
ugaseno_upaljeno = int(input())
l_ = list(map(int, input().split()))
res=0
uzgaseno = 0
for i in range(sijalica):
    if l[i] == 0:
        uzgaseno+=1
for i in range(len(l_)):
    if l[l_[i]] == 1:
        l[l_[i]] = 0
        uzgaseno+=1
    else:
        l[l_[i]] = 1
        uzgaseno-=1
    if uzgaseno==sijalica:
        res+=1
print(res)