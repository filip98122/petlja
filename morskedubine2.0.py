a=int(input())
pos=0
najnize=0
netacno=0
for i in range(a):
    b=int(input())
    pos+=b
    if pos>0:
        netacno=1
    if pos<najnize:
        najnize=pos
if netacno:
    print("-")
else:
    print(najnize)