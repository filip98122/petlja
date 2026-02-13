a,b = map(int, input().split())
for i in range(a):
    c = int(input())
    flasa = c//b
    ostatak = c-(flasa*b)
    res = str(flasa)+" "+str(ostatak)
    print(res)