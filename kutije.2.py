l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
l2.sort()
l3.sort()
l1=min(l2,l3)
l=max(l3,l2)
for i in range(3):
    if l[i]<=l1[i]:
        print("NE")
        exit()
print("DA")