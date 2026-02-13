a=int(input())
if a==1:
    print(-1)
for i in range(1,a+1):
    if i==1:
        continue
    for j in range(1,i):
        if (i+j)%3==0:
            print(f"{i} {j}")