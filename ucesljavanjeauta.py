prvihauta=int(input())
l=[]
for i in range(prvihauta):
    l.append(input())
drugihauta=int(input())
l1=[]
for i in range(drugihauta):
    l1.append(input())
for i in range(min(prvihauta,drugihauta)):
    print(l[i])
    print(l1[i])
if drugihauta>prvihauta:
    for i in range(prvihauta,drugihauta):
        print(l1[i])
elif prvihauta>drugihauta:
    for i in range(drugihauta,prvihauta):
        print(l[i])