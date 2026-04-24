a=int(input().strip())
l=list(map(int,(input().strip()).split()))
pod=2
for i in range(a):
    if l[i]%pod==1:
        print("ne")
        exit()
    pod+=2
    if pod==3:
        pod+=2
    pod%=3
print("da")