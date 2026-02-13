a = int(input())
b = int(input())
l = []
mesto = b+1
for i in range(b):
    aq = int(input())
    l.append(aq)
for i in range(b):
    if a<l[i]:
        mesto-=1
    else:
        break
print(mesto)