__ = int(input())
l=[]
for i in range(__):
    a,b = map(str,input().split())
    b=int(b)
    l1=[b,a]
    l.append(l1)
l.sort(reverse=True)
proslii = 0
prosliivrednost = 0
for i in range(__):
    if i==0:
        pass
    else:
        if l[i][0]==prosliivrednost:
            print(f"{proslii}. {l[i][1]} {l[i][0]}")
            continue
    print(f"{i+1}. {l[i][1]} {l[i][0]}")
    proslii=i+1
    prosliivrednost=l[i][0]