a,b = map(int, input().split())
decaci = []
devojcice = []
for i in range(a):
    decaci.append(input())
for i in range(b):
    devojcice.append(input())
for i in range(a):
    res = decaci[i]
    res = res+" "
    for j in range(b):
        res1 = devojcice[j]
        print(res+res1)
