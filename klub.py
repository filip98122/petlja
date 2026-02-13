__ = int(input())
pre12 = 0
l = []
njkasnijesati = 0
njkasnije = 0
for i in range(__):
    l.append(list(map(int,input().split())))
    if l[i][2]>=njkasnijesati:
        if l[i][2]==njkasnijesati:
            if l[i][3]>njkasnije:
                njkasnije = l[i][3]
        else:
            njkasnije = l[i][3]
            njkasnijesati = l[i][2]
    if l[i][0] <12:
        pre12+=1
l.sort()
g = l[0][0]*60+l[0][1]
h = njkasnijesati*60+njkasnije
e = h-g
njkasnije = e%60
njkasnijesati = e//60
print(f"{njkasnijesati} {njkasnije}")
print(pre12)