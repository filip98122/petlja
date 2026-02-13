a=int(input())
zbir=0
for i in range(a):
    zbir+=int(input())
if zbir%a==0:
    print(int(zbir//a))
else:
    print(int(zbir//a+1))