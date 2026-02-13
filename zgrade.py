a,b = map(int, input().split())
l = []
for i in range(b):
    l.append(int(input()))
l.sort()
iplus = 0
najveca_razlika = 0
zgrada1 = 0
zgrada = 0
prva = 0
druga = 1

while True:
    if druga == len(l)-1:
        break
    d = l[druga]-l[prva]
    if d>a:
        prva+=1
        continue
    if d>najveca_razlika:
        najveca_razlika = d
        zgrada = l[prva]
        zgrada1 = l[druga]
    druga+=1
print(f"{zgrada} {zgrada1}")