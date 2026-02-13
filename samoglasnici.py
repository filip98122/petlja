a = input()
b = input()
c = input()
res = 0
l_a = [*a]
l_b = [*b]
l_c = [*c]
l = [l_a,l_b,l_c]
for i in range(3):
    if l[i][0] == "a" or l[i][0] == "e" or l[i][0] == "i" or l[i][0] == "o" or l[i][0] == "u":
        l[i][0] =1
    else:
        l[i][0] = 0

    if l[i][len(l[i])-1] == "a" or l[i][len(l[i])-1] == "e" or l[i][len(l[i])-1] == "i" or l[i][len(l[i])-1] == "o" or l[i][len(l[i])-1] == "u":
        l[i][len(l[i])-1] =1
    else:
        l[i][len(l[i])-1] = 0
for i in range(3):
    if l[i][0] == 1 and l[i][len(l[i])-1] == 1:
        res+=5
    elif l[i][0] == 1 or l[i][len(l[i])-1] == 1:
        res+=3
    elif l[i][0] != 1 and l[i][len(l[i])-1] != 1:
        res+=1
print(res)