a = input()
d =""
l=[*a]
for i in range(len(l)):
    l[i] = int(l[i])
    l[i]+=1
    l[i] = str(l[i])
    d=d+l[i]
print(d)