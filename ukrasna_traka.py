a = input()
b = int(input())
b-=1
l = [*a]
d ="*"
breakk = 0
res = d
a_l = len(a)
while True:
    for i in range(a_l):
        if b>1:
            res = res+l[i]
        else:
            res=res+d
            breakk = 1
            break
        b-=1
    if breakk==1:
        break
    if b>1:
        res=res+" "
        b-=1
    else:
        res=res+d
        break
    if b==1:
        res=res+d
        break
print(res)