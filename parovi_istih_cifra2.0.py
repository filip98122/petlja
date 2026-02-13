a=input()
b=input()
l=[a,b]
s=dict()
for i in range(2):
    for j in range(2):
        s[l[i][j]]=1
print(4-len(s))