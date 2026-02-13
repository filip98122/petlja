a = int(input())
b = int(input())
c = int(input())
d = int(input())
res=(a+c)/(b+d)
if (a+c)%(b+d) == 0:
    res = int(res)
print(res)