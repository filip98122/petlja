a = int(input())
b = int(input())
aa = "am"
g = " "
if a == 0 and b == 0:
    aa = "am"
if a == 0:
    a = 12
    if b !=0:
        aa = "am"
elif a>=12:
    aa = "pm"
    if a != 12:
        a-=12
ga = str(a)
b = str(b)
d = ga+g+b+g+aa
print(d)