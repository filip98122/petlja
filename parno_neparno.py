__ = int(input())
l = list(map(int, input().split()))
for i in range(__):
    if i%2==l[i]%2:
        continue
    print("ne")
    exit()
print("da")