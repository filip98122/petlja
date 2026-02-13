a=int(input())
for i in range(a):
    a1,b1=map(int,input().split())
    if i==0:
        left=a1
        right=b1
    left=max(left,a1)
    right=min(right,b1)
print(max(right-left+1,0))