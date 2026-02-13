__ = int(input())
najveci = 0
broj = 0
for i in range(__):
    a = int(input())
    if a>=najveci:
        najveci = a
        broj = i+1
print(broj)