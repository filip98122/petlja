a= int(input())
l1 = []
for i in range(a):
    b = input()
    l1.append(b)
y = len(l1[0])
for i in range(a):
    if i == 0:
        continue
    L =[*l1[i]]
    l =[*l1[i-1]]
    razlika = 0
    for j in range(y):
        if L[j] == l[j]:
            continue
        else:
            razlika+=1
    if razlika == 0 or razlika>1:
        print('ne')
        exit()
print('da')
