a=0
b=0

var1=int(input())
var2=int(input())
if var1==0:
    a=0
elif var1==1:
    a=15
elif var1==2:
    a=30
elif var1>=3:
    a=40
    if var1>var2 and a >=4:
        a="ad"
if var2==0:
    b=0
elif var2==1:
    b=15
elif var2==2:
    b=30
elif var2>=3:
    b=40
    if var2>var1 and b>=4:
        b="ad"
print(f"{a}:{b}")