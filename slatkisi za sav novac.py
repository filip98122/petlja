t=int(input())
la=list(map(int,input().split()))
l=[]
zbir=0
zbir1=0
for i in range(t):
    zbir+=la[i]
    l.append([zbir,zbir1])
    zbir1+=la[i]
b=int(input())
for j in range(b):
    c,d=map(int,input().split())
    res=0
    left=c
    right=len(l)-1
    if l[right][0]-l[left][1]<=d:
        print(right-left+1)
        continue
    if l[left][0]-l[left][1]>d:
        print(0)
        continue
    while True:
        sad=(left+right)//2
        if l[sad][0]-l[c][1]<=d and l[sad+1][0]-l[c][1]>d:
            print(sad-c+1)
            break
        if l[sad][0]-l[c][1]>d:
            right=sad
        else:
            left=sad
        if left==right-1:
            pros=(left+right)//2-1
            bud=(left+right)//2+1
            if l[pros][0]-l[c][1]<=d and l[sad][0]-l[c][1]>d:
                print(sad-c)
            elif l[bud][0]-l[c][1]<=d and l[bud+1][0]-l[c][1]>d:
                print(bud-c+1)
            break