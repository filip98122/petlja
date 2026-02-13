a = int(input())
l = list(map(int,input().split()))
res = 0
for i in range(a):
    if i == 0:
        continue
    if l[i-1]<l[i]:
        continue
    res+=l[i-1]-l[i]+1
    l[i] = l[i-1]+1
print(res)