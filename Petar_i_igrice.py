__ = int(input())
res = 0
res1 = 0
for i in range(__):
    a,b,c,d = map(int,input().split())
    res+=c-a
    res1 += d-b
res*=60
res1+=res
res = res1//60
res1 = res1%60

print(f"{res} {res1}")