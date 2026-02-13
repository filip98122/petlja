dani=int(input())
icount=0
najveci=-1
for i in range(dani):
    a=int(input())
    if a>=najveci:
        najveci=a
        icount=i+1
print(icount)