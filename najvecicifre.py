a=input()
l=[*a]
l.sort(reverse=True)
b=""
for i in range(len(l)):b+=l[i]
print(int(b))