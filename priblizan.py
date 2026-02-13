a=int(input())
l=list(map(int,input().split()))
sumacelo=0
priblizno=0
for i in range(a):
    sumacelo+=l[i]
    if l[i]%100>=50:
        priblizno+=(l[i]//100+1)*100
    else:
        priblizno+=(l[i]//100)*100
print(sumacelo)
print(priblizno)