a=int(input())
import sys
sys.setrecursionlimit(5001)
l=list(map(int,input().split()))
l1=[]
for i in range(a):
    l1.append([l[i]/(i+1),i])
l1.sort(reverse=True)
d=0
def rec(para,index,uku):
    if index==len(l):
        return uku
    if para<l1[index][1]+1:
        if index==len(l)-1 or para==0:
            return uku
        return rec(para,index+1,uku)
    f=rec(para-1-l1[index][1],index,uku+l[l1[index][1]])
    g=rec(para,index+1,uku)
    return max(f,g,uku)
b=rec(a,0,0)
print(str(b).strip())