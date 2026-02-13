n=int(input())
l=list(map(int,input().split()))
res=0
if n==1:
    if sum(l)==0:
        res+=1
    print(res)
    exit()
def rec(l,index,zbir):
    global res
    if index==len(l):
        if zbir==0:
            res+=1
        return
    rec(l,index+1,zbir)
    rec(l,index+1,zbir+l[index])
rec(l,0,0)
print(res)