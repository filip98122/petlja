a = int(input())
b = int(input())
k = int(input())
res = 0
res1 = 0
if a>b:
    if a-b>=k:
        res+=k
        k = 0
    else:
        res+=a-b
        k-=a-b
elif b>a:
    if b-a>=k:
        res1+=k
        k = 0
    else:
        res1+=b-a
        k-=b-a
elif a==b:
    res+=k//2
    res1+=k//2
    k = 0
if k!=0:
    res+=k//2
    res1+=k//2
    k = 0
print(res)
print(res1)