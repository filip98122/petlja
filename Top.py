a = input()
l =[*a]
linija =l[0]
horizonta = l[1]
b = int(input())
for i in range(b):
    d = input()
    l =[*d]
    linija_ = l[0]
    horizonta_ = l[1]
    if horizonta == horizonta_ or linija == linija_:
        print("DA")
    else:
        print("NE")