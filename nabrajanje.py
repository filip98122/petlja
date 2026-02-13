l = []
while True:
    a = input()
    if a == "gotovo":
        break
    else:
        l.append(a)
res = ""
for i in range(len(l)):
    if i == len(l)-1:
        if len(l) != 1:
            res = res+" i "+l[i]
        else:
            res = l[i]
    elif i == 0:
        res = res+l[i]
    else:
        res = res+", "+l[i]
print(res)