a = int(input())
b = int(input())
c = int(input())
d = int(input())
povecanje = max(a,b)-min(a,b)
trenutno = min(a,b)*c
res=0
while trenutno<d:
    trenutno+=povecanje
    res+=1
if trenutno==d:
    pass
else:
    print(0)
    print(0)
    exit()
if max(a,b) ==a:
    print(res)
    print(c-res)
else:
    print(c-res)
    print(res)