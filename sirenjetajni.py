ucenika=int(input())
pratiocib=int(input())
pozprat=list(map(int,input().split()))
rasporeda=int(input())
pozprat.sort()
for i in range(rasporeda):
    a=int(input())
    if a<pozprat[0]:
        print(pozprat[0]-1)
        continue
    if a>pozprat[-1]:
        print(ucenika-pozprat[-1])
        continue
    left=0
    right=len(pozprat)-1
    while True:
        mid=(right+left)//2
        if mid+1==len(pozprat):
            val=ucenika+1
        else:
            val=pozprat[mid+1]
        if pozprat[mid]<a<val:
            print(val-pozprat[mid]-1)
            break
        if left==right-1:
            break
        if pozprat[mid]>a:
            right=mid
        else:
            left=mid