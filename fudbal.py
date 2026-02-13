A = 0
B = 0
C = 0
D = 0
a = 0
b = 0
c = 0
d = 0
a1 = 0
b1 = 0
c1 = 0
d1 = 0

def p(e1,e2):
    if e1>e2:
        e1 =3
        e2 = 0
    elif e1==e2:
        e1 = 1
        e2 = 1
    elif e2>e1:
        e1 = 0
        e2 = 3
    return e1,e2

for i in range(6):
    e11,e21 = map(int, input().split())
    e1,e2 = p(e11,e21)
    if i == 0:
        A+=e1
        B+=e2
        a+=e21
        b+=e11
        a1+=e11
        b1+=e21
    if i == 1:
        C+=e1
        D+=e2
        c+=e21
        d+=e11
        c1+=e11
        d1+=e21
    if i == 2:
        A+=e1
        C+=e2
        a+=e21
        c+=e11
        a1+=e11
        c1+=e21
    if i == 3:
        B+=e1
        D+=e2
        b+=e21
        d+=e11
        b1+=e11
        d1+=e21
    if i == 4:
        A+=e1
        D+=e2
        a+=e21
        d+=e11
        a1+=e11
        d1+=e21
    if i == 5:
        B+=e1
        C+=e2
        b+=e21
        c+=e11
        b1+=e11
        c1+=e21
print(f"{A} {a1-a}")
print(f"{B} {b1-b}")
print(f"{C} {c1-c}")
print(f"{D} {d1-d}")