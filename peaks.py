a = int(input())
l = list(map(int, input().split()))
peaks = 0
for i in range(a):
    if i == 0:
        if l[i]>l[i+1]:
            peaks+=1
            continue
    if i == a-1:
        if l[i]>l[i-1]:
            peaks+=1
            continue
    if l[i]>l[i-1]:
        if l[i]>l[i+1]:
            peaks+=1
print(peaks)