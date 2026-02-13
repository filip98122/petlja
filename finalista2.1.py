a=int(input().strip())
b=int(input().strip())
c=int(input().strip())
d=int(input().strip())
trazen=min(max(a,b),max(c,d))
l=[a,b,c,d]
abcd="ABCD"
for i in range(4):
    if trazen==l[i]:
        print(abcd[i])