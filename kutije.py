l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l.sort()
l1.sort()
for i in range(3):
    if l[i]>l1[i]:
        if i == 2:
            print("DA")
            exit()
        pass
    else:
        pass
for i in range(3):
    if l[i]<l1[i]:
        if i == 2:
            print("DA")
            exit()
        pass
    else:
        pass
print("NE")