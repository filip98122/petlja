a,b,c = map(int,input().split())   
skije = [] 
pancerice = [] 
for i in range(b): 
    skije.append(int(input())) 
for i in range(c): 
    pancerice.append(int(input())) 

i = 0  
j = c-1
skije.sort()
pancerice.sort()
res = 0
while True:
    if j == -1 or i == b:
        break
    curent = skije[i]+pancerice[j]
    if curent>a:
        j-=1
    else:
        if res <curent:
            res = curent
        i+=1
print(a-res)