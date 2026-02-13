a=input().strip()
l=[*a]
res=""
for i in range(len(l)):
    b=int(l[i])
    b+=1
    res=res+str(b)
print(res)