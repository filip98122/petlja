l = []
for i in range(3):
    if i == 0:
        prva,druga = map(str,input().split())
        l.append(prva)
        l.append(druga)
        continue
    d,c = map(str,input().split())
    l.append(d)
    l.append(c)
kolko_puta = 0
for i in range(6):
    if l[i] == prva:
        kolko_puta+=1
if kolko_puta==3:
    print(prva)
    exit()
kolko_puta = 0
for i in range(6):
    if l[i] == druga:
        kolko_puta+=1
if kolko_puta == 3:
    print(druga)
else:
    print("nemoguce")