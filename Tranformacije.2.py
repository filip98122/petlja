a=int(input())
b=int(input())
for i in range(b):
    a=a*a+1
    a%=1000
a=str(a)
print(a.zfill(3))