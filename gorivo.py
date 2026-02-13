import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a%100==0:
    print(((a//100)*b)+((a//100)*c)+((a//100)*d))
else:
    res = 0
    res+=math.ceil((a/100)*b)
    res+=math.ceil((a/100)*c)
    res+=math.ceil((a/100)*d)
    print(res)