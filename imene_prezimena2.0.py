a,b=map(int,input().split())
l1=[]
l2=[]
for i in range(a):
    l1.append(input())
for i in range(b):
    l2.append(input())
for i in range(a):
    for j in range(b):
        print(f"{l1[i]} {l2[j]}")