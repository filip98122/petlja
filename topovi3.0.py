n=int(input())
l=[]
g=[]
for i in range(n):
    l.append(list(map(int,(input().strip()).split())))
    if sum(l[-1])>1:
        print(1)
        exit()
    g.append(0)
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            if g[j]==0:
                g[j]=1
            else:
                print(1)
                exit()
print(0)