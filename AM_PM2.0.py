a=int(input())
b=int(input())
if a>=12:
    c="pm"
    if a!=12:
        a-=12
else:
    c="am"
if a==0:
    a=12
    c="am"
print(f"{a} {b} {c}")