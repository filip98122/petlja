a=int(input())
b=int(input())
l=[a,b]
c=int(input())
d=int(input())
l.sort()
prvi=d
for i in range(0,1+c):
    if l[0]*(c-i)+l[1]*i==d:
        if a>b:
            print(i)
            print(c-i)
        else:
            print(c-i)
            print(i)
        exit()
for i in range(2):print(0)