a,s,b,s,c=map(str,input().split())
a1,s,b1,s,c1=map(str,input().split())
l=[a,b,c]
l1=[a1,b1,c1]
lstvari=[["0"],["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]
for i in range(3):
    for j in range(len(l1[i])):
        if len(lstvari[int(l1[i][j])])==1:
            lstvari[int(l1[i][j])].append(l[i][j])
        else:
            if lstvari[int(l1[i][j])][1]!=l[i][j]:
                print('ne')
                exit()
for i in range(len(lstvari)):
    pamti=i
    if len(lstvari[pamti])==1:
        continue
    for j in range(len(lstvari)):
        if j==pamti:
            continue
        if len(lstvari[j])==1:
            continue
        if lstvari[pamti][1]==lstvari[j][1]:
            print('ne')
            exit()
print("da")