a,b,c,d=map(int,input().split())
l=[a,b,c,d]
ls=sorted(l)
lod=["a","b","c","d"]
more1=False
if 100>=ls[-1]*2:
    more1=True
if more1:
    a1,b1=map(str,input().split())
    ind1=lod.index(a1)
    ind2=lod.index(b1)
    if max(l[ind1],l[ind2])-min(l[ind1],l[ind2])>=20:
        print(lod[l.index(max(l[ind1],l[ind2]))])
    else:
        print(input())
else:
    print(lod[l.index(max(l))])