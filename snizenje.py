__ = int(input())
res = 0
for i in range(__):
    a,b = map(int, input().split())
    res+=a-(a*(b/100))
print('{0:.2f}'.format(res))