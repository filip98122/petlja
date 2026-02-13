l = [int(input()),int(input()),int(input())]
l.sort()
najmanji = l[0]
if l[2]-l[1]-l[0]>0:
    if l[2]-l[1]-l[0]<najmanji:
        najmanji = l[2]-l[1]-l[0]
if l[1]-l[0]>0:
    if l[1]-l[0]<najmanji:
        najmanji = l[1]-l[0]
if l[2]-l[0]>0:
    if l[2]-l[0]<najmanji:
        najmanji = l[2]-l[0]
if l[2]-l[1]>0:
    if l[2]-l[1]<najmanji:
        najmanji = l[2]-l[1]
if l[0]+l[1]-l[2]>0:
    if l[0]+l[1]-l[2]<najmanji:
        najmanji = l[0]+l[1]-l[2]
print(najmanji)