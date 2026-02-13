a = int(input())
b = int(input())
c = int(input())
g = input()
l = [*g]
res = 0
for i in range(len(l)):
    if l[i] =="j":
        res+=a
    elif l[i]=="k":
        res+=b
    else:
        res+=c
print(res)