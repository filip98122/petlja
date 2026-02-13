a,b=map(str,input().split())
b=int(b)
if b==0:
    print(a)
    exit()
l=[*a]
sati = l[0]+l[1]
sati=int(sati)
minuti=l[3]+l[4]
minuti=int(minuti)
minuti+=sati*60
sati =0
minuti-=b
if minuti<=120 and minuti+b > 120:
    minuti+=60
if minuti//60>9:
    if minuti%60>9:
        print(f"{minuti//60}:{minuti%60}")
    else:
        print(f"{minuti//60}:0{minuti%60}")
else:
    if minuti>9:
        print(f"0{minuti//60}:{minuti%60}")
    else:
        print(f"0{minuti//60}:0{minuti%60}")