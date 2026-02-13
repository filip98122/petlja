a = input()
b = int(input())
b-=1
l = [*a]
res = "*"
while True:
    if b == 1:
        res = res+"*"
        b-=1
        print(res)
        exit()
    for i in range(len(l)):
        if b>1:
            res = res+l[i]
            b-=1
        if b == 1 or b == 0:
            res = res+"*"
            print(res)
            exit()
    if b>1:
        res=res+" "
        b-=1
