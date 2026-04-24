a,b,c,d=map(int,(input().strip()).split())
tez1,tez2=map(int,(input().strip()).split())
brojevi=[a,b,c,d]
l=[]
for i in range(4):
    l.append([brojevi[i],[i]])
    for i2 in range(4):
        if i>=i2:continue
        l.append([brojevi[i]+brojevi[i2],[i,i2]])
l.sort()
najmanje=a+b+c+d
suma=a+b+c+d
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            continue
        nova=[]+l[i][1]+l[j][1]
        nova=set(nova)
        if len(nova)==len(l[i][1])+len(l[j][1]):
            tren=0
            if tez1>=l[i][0]:
                tren+=l[i][0]
            if tez2>=l[j][0]:
                tren+=l[j][0]
            najmanje=min(najmanje,suma-tren)
print(najmanje)