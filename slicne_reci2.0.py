t=int(input())
l=[]
for i in range(t):
    l.append(input().strip())
lenw=len(l[0])
for i in range(t):
    razlika=0
    if i==0:
        continue
    for j in range(lenw):
        if l[i][j]!=l[i-1][j]:
            razlika+=1
    if razlika>1 or razlika==0:
        print("ne")
        exit()
print("da")