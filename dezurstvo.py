__ = int(input())
res = 0
res1 = 0
for i in range(__):
    s = input()
    l = [*s]
    a = int(input())
    res1+=a
    l1 = list(map(int, input().split()))
    for i in range(a):
        if l[l1[i]] == "D":
            res+=1
print(f"{res1} {res}")