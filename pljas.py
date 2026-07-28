a=int(input())
res=0
for i in range(a):
    b=int(input())
    c=str(b)
    if b%3==0 or c[-1]=="3":
        res+=1
print(res)