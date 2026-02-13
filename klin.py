prethodna=""
t=int(input())
lose=False
obrnuto=False
pola=0
for i in range(t):
    a=input()
    if i==0 or lose:
        if len(a)!=t:
            lose=True
        prethodna=a
        continue
    if len(prethodna)-1!=len(a):
        lose=True
        continue
    try:
        if prethodna.index("".join(reversed(a))):
            pass
    except:
        try:
            if prethodna.index(a):
                pass
        except:
            lose=True
            continue
    prethodna=a
if lose:print("NE")
else:print("DA")