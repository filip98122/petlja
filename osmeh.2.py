a=input().strip()
osmeh=False
kolko=0
for i in range(len(a)):
    if osmeh:
        if a[i]==")":
            kolko+=1
        else:
            osmeh=False
            if kolko>0:
                print(("OSM"+("E"*kolko)+"H").strip())
            kolko=0
    if a[i]==":":
        osmeh=True
        continue
if kolko>0:
    print(("OSM"+("E"*kolko)+"H").strip())