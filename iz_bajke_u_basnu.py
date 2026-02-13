l = []
for i in range(4):
    a = int(input())
    l.append(a)
l.sort()
napred = l[3]+l[1]
nazad = l[0]+l[2]
nn = napred-nazad
levo = l[3]+l[0]
desno = l[1]+l[2]
ld =levo-desno
if nn>ld:
    print(nn)
else:
    print(ld)