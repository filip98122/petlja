l=[]
for i in range(4):
    l.append(int(input()))
l.sort()
print(l[1]-l[0]+l[3]-l[2])