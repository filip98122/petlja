a=int(input())
b=int(input())
kazalkapravac=True
l=[]
index=0
for i in range(1,a+1):
    l.append([i,True])
izbacenih=a
while len(l)>1:
    count=b
    while True:
        if kazalkapravac:
            index%=a
            if not l[index][1]:
                index+=1
            else:
                if count>1:
                    index+=1
                    count-=1
                else:
                    break
        else:
            index%=a
            if not l[index][1]:
                index-=1
            else:
                if count>1:
                    index-=1
                    count-=1
                else:
                    break
    index%=a
    print(l[index][0])
    l[index][1]=False
    kazalkapravac=not kazalkapravac
    izbacenih-=1
    if izbacenih==0:
        break