izmedu=list(map(str,input().split()))
najmanji=""
najveci=""
l=[]
for i in range(4):
    if izmedu[i].strip()==">":l.append(True)
    else:l.append(False)
if l[0]:najveci+="a"
else:najmanji+="a"



#Drugi 
if l[0]:
    if l[1]:pass
    else:najmanji+="b"
else:
    if l[1]:najveci+="b"
    else:pass
da=1
oz="c"
if l[0+da]:
    if l[1+da]:pass
    else:najmanji+=oz
else:
    if l[1+da]:najveci+=oz
    else:pass
da=2
oz="d"
if l[0+da]:
    if l[1+da]:pass
    else:najmanji+=oz
else:
    if l[1+da]:najveci+=oz
    else:pass
if l[3]:najmanji+="e"
else:najveci+="e"
print(najmanji)
print(najveci)