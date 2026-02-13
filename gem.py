a = int(input())
b = int(input())
aa = 0
bb = 0
if a ==1:
    aa = 15
if b == 1:
    bb =15
if b ==2:
    bb = 30
if a == 2:
    aa = 30
if a == 3:
    aa = 40
if b == 3:
    bb = 40
if a>3:
    if a-b!=0 and a-b>0:
        aa = "ad"
if b>3:
    if b-a!=0 and b-a>0:
        bb = "ad"
if aa == "ad":
    bb =40
if bb == "ad":
    aa=40

if a>=3 or b>=3:
    if a == b:
        aa = 40
        bb = 40

aa = str(aa)
bb = str(bb)
print(aa+":"+bb)