a,b = map(float, input().split())
c,d = map(float, input().split())
gore=(d-b)
c,d = map(float, input().split())
c,d = map(float, input().split())
if d<0:
    d*=-1
levo=d
print('{0:.4f}'.format(gore+(levo*2)))