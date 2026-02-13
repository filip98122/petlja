a=int(input())
if a==1:
    print(int(input()))
    print("da")
    exit()
l=[]

l1=[]
for i in range(a):
    l.append(list(map(int,input().split())))
    l1.append([0,i])
for i in range(a):
    for j in range(a):
        l1[i][0]+=l[j][l1[i][1]]#Treba value += value of square
        l1[i][1]+=1
        if l1[i][1]==a:#reset
            l1[i][1]-=a

konacno="da"


for i in range(a):
    print(l1[i][0])
    if l1[0][0]==l1[i][0]:
        pass
    else:
        konacno="ne"
print(konacno)