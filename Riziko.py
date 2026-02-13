a=int(input())
l=list(map(int,input().split()))
b=int(input())
la=list(map(int,input().split()))
res=0
res1=0
l.sort(reverse=True)
la.sort(reverse=True)
for i in range(min(a,b)):
    if l[i]>la[i]:res+=1
    else:res1+=1
print(f"{res1} {res}")