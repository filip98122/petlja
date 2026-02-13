a=int(input())#j
b=int(input())#k
c=int(input())#l
l=input()
res=0
for i in range(len(l)):
    if l[i]=="j":
        res+=a
    if l[i]=="k":
        res+=b
    if l[i]=="l":
        res+=c
print(res)