a = float(input())
b = float(input())
c = int(input())
print(round(b*c,1))
res=1
if a%(b*c)==0:
    res-=1
print(int(((b*c)//a)+res))