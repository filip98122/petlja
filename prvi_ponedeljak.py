a = input()
l = [*a]
b= int(input())
d = 0
for i in range(len(l)):
    if l[d] == "-":
        del l[d]
        d-=1
    d+=1
dani = l[0]+l[1]
mesec = l[2]+l[3]
godina = l[4]+l[5]+l[6]+l[7]

dani = int(dani)
mesec = int(mesec)
godina = int(godina)

dani+=8-b
while dani>=1:
    dani-=7
    if dani<=0:
        dani+=7
        break
if mesec<10:
    print(f"0{dani}-0{mesec}-{godina}")
else:
    print(f"0{dani}-{mesec}-{godina}")