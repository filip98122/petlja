a,b=map(str,(input().strip()).split())
l=[*a]
najvece=max(l)
for i in range(len(l)):
    if l[i]==najvece:
        l[i]=b
print("".join(l))