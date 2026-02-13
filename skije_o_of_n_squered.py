a,b,c = map(int,input().split())
skije = []
pancerice = []
for i in range(b):
    skije.append(int(input()))
for i in range(c):
    pancerice.append(int(input()))
skije.sort()
pancerice.sort()
najm = 100000000
for i in range(b):
    for j in range(c):
        d = a-(skije[i]+pancerice[j])
        if d>0:
            if d<najm:
                najm = d
print(najm)