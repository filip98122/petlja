a = input()
l = [*a]
vatrica = 0
sm = 0
res = 0
for i in range(len(l)):
    if vatrica==1:
        if l[i]==")":
            sm+=1
        else:
            res = "OSM"
            for ii in range(sm):
                res=res+"E"
            res = res+"H"
            if res!="OSMH":
                print(res)
            vatrica=0
            sm=0
    if l[i] == ":":
        vatrica = 1
res = "OSM"
for ii in range(sm):
    res=res+"E"
res = res+"H"
if res!="OSMH":
    print(res)
vatrica=0
sm=0