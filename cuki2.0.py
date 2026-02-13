duzina,skracenje,broj_zvonca=map(int,input().split())
l=[]
lp=0
rp=duzina
if duzina/skracenje%2==1:
    for i in range(duzina//skracenje):
        if i<=(duzina//skracenje)//2:
            l.append(i*2+1)
        else:
            l.append(((duzina//2-i))*2)
else:
    for i in range(duzina//skracenje):
        if i<(duzina//skracenje)//2:
            l.append(i*2+1)
        else:
            l.append(((duzina//2-i))*2)
            
for i in range(broj_zvonca):
    a=int(input())
    if a==0 or a==duzina or skracenje==duzina:
        print(1)
        continue
    if duzina%skracenje==0:
        if a == duzina//skracenje:
            print(duzina//skracenje)
            continue
    if a%skracenje==0:
        if a//skracenje<(duzina//skracenje)//2:
            print(l[a//skracenje]-1)
        else:
            print(l[(a//skracenje-1)]-1) 
        continue
    print(l[a//skracenje])