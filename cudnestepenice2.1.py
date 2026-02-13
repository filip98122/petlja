a=int(input())
l=list(map(int,input().split()))
res=[1,0]
pocevsi=0
zavrsava=1
razlika=None
for i in range(a):
    if i==0:
        continue
    if razlika==l[i]-l[i-1] or razlika==None:
        zavrsava=i
        razlika=l[i]-l[i-1]
        if zavrsava-pocevsi>res[0]-res[1]:
            res=[zavrsava,pocevsi]
    else:
        pocevsi=i-1
        zavrsava=i
        razlika=l[i]-l[i-1]
print(*l[res[1]:res[0]+1])