h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
h7 = 0
h8 = 0
h9 = 0
h10 = 0
h11 = 0
h12 = 0
__ = int(input())
for i in range(__):
    dan = 0
    mesec = 0
    a = input()
    l= [*a]
    dan = l[0]+l[1]
    dan = int(dan)
    mesec = l[2]+l[3]
    mesec = int(mesec)
    if mesec == 3:
        if dan>=21:
            h1+=1
        else:
            h12+=1
    if mesec == 4:
        if dan>=21:
            h2+=1
        else:
            h1+=1
    if mesec == 5:
        if dan>=22:
            h3+=1
        else:
            h2+=1
    if mesec == 6:
        if dan>=22:
            h4+=1
        else:
            h3+=1
    if mesec == 7:
        if dan>=23:
            h5+=1
        else:
            h4+=1
    if mesec ==8:
        if dan>=23:
            h6+=1
        else:
            h5+=1
    if mesec == 9:
        if dan>=23:
            h7+=1
        else:
            h6+=1
    if mesec == 10:
        if dan>=24:
            h8+=1
        else:
            h7+=1
    if mesec == 11:
        if dan>=23:
            h9+=1
        else:
            h8+=1
    if mesec == 12:
        if dan>=22:
            h10+=1
        else:
            h9+=1
    if mesec == 1:
        if dan>=21:
            h11+=1
        else:
            h10+=1
    if mesec == 2:
        if dan>=20:
            h12+=1
        else:
            h11+=1
print(h1)
print(h2)
print(h3)
print(h4)
print(h5)
print(h6)
print(h7)
print(h8)
print(h9)
print(h10)
print(h11)
print(h12)