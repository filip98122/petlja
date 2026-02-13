a = input()
b = input()
l = [*a]
l1 = [*b]
for i in range(2):
    l[i] = int(l[i])
    l1[i] = int(l1[i])
l.sort()
l1.sort()
g=0
res = 0
for i in range(2):
    if l[0]==l1[g]:
        res+=1
        del l[0]
        del l1[g]
        break
    g+=1
if res == 0:
    g=0
    for i in range(2):
        if l[1]==l1[g]:
            res+=1
            del l[1]
            del l1[g]
            break
        g+=1
else:
    if l[0]==l1[0]:
        res+=1
print(res)