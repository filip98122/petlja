a,b = map(int, input().split())
a = str(a)
b = str(b)
l=[*a]
najveca_cifra = 0
res = ""
for i in range(len(l)):
    l[i] = int(l[i])
    if najveca_cifra<l[i]:
        najveca_cifra = l[i]
    l[i] = str(l[i])
najveca_cifra = str(najveca_cifra)
for i in range(len(l)):
    if l[i] ==najveca_cifra:
        l[i] = b
    res = res+l[i]
print(res)