__ = int(input())
nivo = 0
naj = 0
for i in range(__):
    a =int(input())
    nivo+=a
    if nivo>0:
        print("-")
        exit()
    if naj>nivo:
        naj = nivo
print(naj)