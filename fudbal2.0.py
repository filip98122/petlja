Agol=0
Apri=0
Bgol=0
Bpri=0
Cgol=0
Cpri=0
Dgol=0
Dpri=0
def poeni(r1,r2):
    p1=0
    p2=0
    if r1>r2:
        p1=3
        p2=0
    elif r1==r2:
        p1=1
        p2=1
    else:
        p1=0
        p2=3
    return p1,p2
for i in range(6):
    t1,t2=map(int,input().split())
    p1,p2=poeni(t1,t2)
    if i==0:
        Agol+=p1
        Bgol+=p2
        Apri+=t1-t2
        Bpri+=t2-t1
    if 1==i:
        Cgol+=p1
        Dgol+=p2
        Cpri+=t1-t2
        Dpri+=t2-t1
    if i==2:
        Agol+=p1
        Cgol+=p2
        Apri+=t1-t2
        Cpri+=t2-t1
    if i==3:
        Bgol+=p1
        Dgol+=p2
        Bpri+=t1-t2
        Dpri+=t2-t1
    if 4==i:
        Agol+=p1
        Dgol+=p2
        Apri+=t1-t2
        Dpri+=t2-t1
    if 5==i:
        Bgol+=p1
        Cgol+=p2
        Bpri+=t1-t2
        Cpri+=t2-t1
print(f"{Agol} {Apri}")
print(f"{Bgol} {Bpri}")
print(f"{Cgol} {Cpri}")
print(f"{Dgol} {Dpri}")