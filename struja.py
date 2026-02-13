__,b = map(int, input().split())
l = []
for i in range(__):
    l.append(float(input()))
a = int(input())

l2 = []
for i in range(__):
    l2.append(0)
for i in range(a):
    s = list(map(float, input().split()))
    for j in range(__):
        if s[0]<= j+1 and s[1]>=j+1:
            l2[j]+=1
for i in range(__):
    if l2[i]==0:
        print('{0:.2f}'.format(0))
        continue
    print('{0:.2f}'.format((l[i]*b)/l2[i]))