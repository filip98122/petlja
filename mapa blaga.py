l=[
    [
        ["propast","propast"],
        ["R","K"]
    ],
    [
        ["M","propast"],
        ["Z","T"]
    ]
]
a=input()
b=input()
c=input()
l2=[a,b,c]
for i in range(3):
    if l2[i]=="L":
        l2[i]=0
    else:
        l2[i]=1
print(l[l2[0]][l2[1]][l2[2]])