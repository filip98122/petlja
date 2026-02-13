l = []
for i in range(26):
    l.append(list(map(str, input().split())))
a = int(input())
res=""
def convert(c,d):
    h = "abcdefghijklmnopqrstuvwxyz"
    c = h.index(c)
    d = h.index(d)
    return c,d
for i in range(a):
    c = input()
    l2 = [*c]
    e,g = convert(l2[0],l2[1])
    slv = l[e][g]
    res=res+slv
print(res)