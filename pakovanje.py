a = int(input())
b = int(input())
c = int(input())
ab = a*b
bc = b*c
ac = a*c
res=ab+bc+ac
res*=2
res+=min(ab,bc,ac)
print(res)