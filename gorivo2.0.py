a=int(input())
l=[int(input()),int(input()),int(input())]
res=0
for i in range(3):
    temp=(a/100)*l[i]
    strtemp=str(temp)
    res+=int(temp)
    if strtemp[len(strtemp)-1]!="0":
        res+=1
print(res)