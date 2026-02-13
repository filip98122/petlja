l = []
l1 = []
for i in range(4):
    a,b = map(int, input().split())
    l.append(a)
    l1.append(b)
najveci = 0
for i in range(3):
    if i == 0:
        najveci = l[i]
    if l[i+1]-l1[i]>najveci:
        if l[i+1]>l1[i]:
            najveci = l[i+1]-l1[i]
print(najveci)