res=0
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
res+=a
res+=b
res+=c
res+=d
res+=e
res/=5
if res>=4.4:
    print(5)
    exit()
elif res>=3.4:
    print(4)
    exit()
elif res>=2.4:
    print(3)
    exit()
elif res>=1.4:
    print(2)
    exit()
else:
    print(1)