a = int(input())
l = []
res = 0
iplus = 0
vatra = 0
vatrica = 0
l = list(map(int,input().split()))
for i in range(a):
    if i == 0 or i == a-1:
        continue
    predhodni = l[i-1]
    if predhodni>l[i]:
        vatra = 1
    if predhodni!=l[i] or predhodni == l[i]:
        if l[i+1]>l[i]:
            if vatra==1:
                res+=1
                vatra = 0
        if predhodni!=l[i] and predhodni<l[i]:
            vatra = 0
print(res)