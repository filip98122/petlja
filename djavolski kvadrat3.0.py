a=int(input())
l=[]
g=[]
leftright=[]
rightleft=[]
sumslevodesno=[]
for i in range(a):
    l.append(list(map(int,(input().strip()).split())))
    g.append(0)
    leftright.append(0)
    rightleft.append(0)
S=sum(l[0])
for i in range(a):
    sumcurrent=0
    for j in range(a):
        g[j]+=l[i][j]
        sumcurrent+=l[i][j]
        koji_left_right=j-i
        koji_left_right+=a
        koji_left_right%=a
        leftright[koji_left_right]+=l[i][j]
        ind=j+i
        ind%=a
        rightleft[ind]+=l[i][j]
        
    sumslevodesno.append(sumcurrent)
for i in range(a):
    if sumslevodesno[i]==S==g[i]:
        pass
    else:
        print("nije ni magican ni djavolski")
        exit()
if not (leftright[0]==S==rightleft[-1]):
    print("nije ni magican ni djavolski")
    exit()
for i in range(a):
    if leftright[i]==S==rightleft[i]:
        pass
    else:
        print("jeste magican ali nije djavolski")
        exit()
print("djavolski")