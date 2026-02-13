a = int(input())
l = [0,0,0,0,0,0,0,0]
for i in range(a):
    s,b = map(float, input().split())
    s = int(s)
    s-=1
    if b>=4.50:
        l[s]+=1
najbolje_odeljenje = 0
petica = 0
for i in range(8):
    if l[i]>petica:
        najbolje_odeljenje = i+1
        petica=l[i]
    if l[i]==petica:
        najbolje_odeljenje = i+1
print(najbolje_odeljenje)