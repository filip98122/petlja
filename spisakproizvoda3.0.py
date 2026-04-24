a=int(input())
b=int(input())
c=int(input())
s=input()
res=0
for i in range(len(s)):
    if s[i]=="j":
        res+=a
        continue
    if s[i]=="k":
        res+=b
        continue
    res+=c
print(res)