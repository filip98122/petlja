x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())     
x3,y3 = map(float, input().split())
x4,y4 = map(float, input().split())

def proveralinija(x1,y1,x2,y2,x3,y3,x4,y4):
    if x3<x1<x4 and x3<x2<x4 and y1<y3<y2 and y1<y4<y2:
        return True
    if y3<y1<y4 and y3<y2<y4 and x1<x3<x4 and x1<x4<x2:
        return True
    return False
def proveravanje(x1,y1,x2,y2,topeleft,bottomright):
    if proveralinija(x1,y1,x2,y2,topeleft[0],topeleft[1],topeleft[0],bottomright[1]) or proveralinija(x1,y1,x2,y2,topeleft[0],topeleft[1],bottomright[0],topeleft[1]) or proveralinija(x1,y1,x2,y2,topeleft[0],bottomright[1],bottomright[0],bottomright[1]) or proveralinija(x1,y1,x2,y2,bottomright[0],topeleft[1],bottomright[0],bottomright[1]):
        return True
    return False
if (not proveravanje(x1,y1,x1,y2,[x3,y3],[x4,y4]) and not proveravanje(x1,y2,x2,y2,[x3,y3],[x4,y4])) or (not proveravanje(x1,y1,x2,y1,[x3,y3],[x4,y4]) and not proveravanje(x2,y1,x2,y2,[x3,y3],[x4,y4])):
    print(abs(x1-x2)+abs(y1-y2))