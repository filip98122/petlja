a = input()
l=[input(),input(),input()]
def konvert(l1,a):
    if l1[0] == a:
        if l1[1] == "A":
            l1[1] = 150
        elif l1[1] == "K":
            l1[1] = 140
        elif l1[1] == "Q":
            l1[1] = 130
        elif l1[1] == "J":
            l1[1] = 120
        elif len(l1) == 3:
            l1[1] = 100
        elif l1[1] ==1:
            l1[1] = 16
        else:
            l1[1] = int(l1[1])
            l1[1]=l1[1]*10
    else:
        if l1[1] == "A":
            l1[1] = 15
        if l1[1] == "K":
            l1[1] = 14
        if l1[1] == "Q":
            l1[1] = 13
        if l1[1] == "J":
            l1[1] = 12
aduta = 0
najveci = 0
res = 0
for i in range(3):
    l1=[*l[i]]
    if l1[0]==a:
        aduta+=1
if aduta == 0:
    l1 = [*l[0]]
    a = l1[0]
for i in range(3):
    l1=[*l[i]]
    konvert(l1,a)
    l1[1] = int(l1[1])
    if najveci<l1[1]:
        najveci = l1[1]
        res=i+1
print(res)