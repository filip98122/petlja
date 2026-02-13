a=int(input().strip())
l1=list(map(int,(input().strip()).split()))
b=int(input().strip())
l2=list(map(int,(input().strip()).split()))
for i in range(a):
    for j in range(b):
        if l1[i]!=l2[j]:
            print(f"{l1[i]} {l2[j]}")