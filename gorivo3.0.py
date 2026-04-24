a=int(input())
import math
res=0
for i in range(3):
    res+=math.ceil((a/100)*(int(input())))
print(res)