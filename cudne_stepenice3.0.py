a=int(input().strip())
l=list(map(int,(input().strip()).split()))
mapoc=0
makraj=0
pocetak=0
kraj=0
razlika=l[1]-l[0]
for i in range(1,a):
    if razlika==l[i]-l[i-1]:
        kraj=i
        if kraj-pocetak>makraj-mapoc:
            makraj=kraj
            mapoc=pocetak
    else:
        razlika=l[i]-l[i-1]
        pocetak=i-1
        kraj=i
ono=l[mapoc:makraj+1]
sttring=""
for i in range(len(ono)):
    sttring=sttring+str(ono[i])
    sttring=sttring+" "
print(sttring.strip())