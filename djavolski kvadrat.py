n=int(input())
if n==1:
    print("djavolski")
    exit()
suma=0
redovi=[]
krive=[]
dva=[0,0]
ind1=0
ind2=n-1

for i in range(n):
    l=list(map(int,input().split()))
    if i==0:
        suma=sum(l)
    if sum(l)!=suma:
        print("nije ni magican ni djavolski")
        exit()
    dva[0]+=l[ind1]
    dva[1]+=l[ind2]
    ind1+=1
    ind2-=1
    for j in range(n):
        if i==0:
            redovi.append(l[j])
            if j!=0:
                krive.append([l[j],j,1])
            if j!=n-1:
                krive.append([l[j],j,-1])
            
        else:
            redovi[j]+=l[j]
            if j==0:
                krive[0][1]+=krive[0][2]
                if krive[0][1]==-1:
                    krive[0][1]+=n
                    krive[0][0]+=l[krive[0][1]]
                    continue
                krive[0][0]+=l[krive[0][1]]
            elif j==n-1:
                krive[-1][1]+=krive[-1][2]
                if krive[-1][1]==n:
                    krive[-1][1]-=n
                    krive[-1][0]+=l[krive[-1][1]]
                    continue
                krive[-1][0]+=l[krive[-1][1]]
                
                
            else:
                krive[j*2][1]+=krive[j*2][2]
                if krive[j*2][1]==-1:
                    krive[j*2][1]+=n
                    krive[j*2][0]+=l[krive[j*2][1]]
                else:
                    krive[j*2][0]+=l[krive[j*2][1]]
                krive[j*2-1][1]+krive[j*2-1][2]
                if krive[j*2-1][1]==n:
                    krive[j*2-1][1]-=n
                    krive[j*2-1][0]+=l[krive[j*2-1][1]]
                else:
                    krive[j*2-1][0]+=l[krive[j*2-1][1]]
for i in range(n):
    if redovi[i]==suma:
        pass
    else:
        print("nije ni magican ni djavolski")
        exit()
if dva[0]!=suma or dva[1]!=suma:
    print("nije ni magican ni djavolski")
    exit()
for i in range(len(krive)):
    if krive[i][0]==suma:
        pass
    else:
        print("jeste magican ali nije djavolski")
        exit()
print("djavolski")