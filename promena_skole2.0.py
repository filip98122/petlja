import math
def truncate(f, n):
    return math.trunc(f * 10**n) / 10**n
predmeta_iz_med_skole = int(input())
neracunajuci_predmeti = int(input())
l = []
for i in range(neracunajuci_predmeti):
    ocena_za_taj_predmet = int(input())
    l.append(ocena_za_taj_predmet)
prosek = float(input())
proseknepodeljen=prosek*predmeta_iz_med_skole
proseknepodeljen=round(proseknepodeljen)
for i in range(neracunajuci_predmeti):
    proseknepodeljen-=l[i]
prosek=str(proseknepodeljen/(predmeta_iz_med_skole-neracunajuci_predmeti))
if len(prosek)==1:
    prosek= prosek+".00"
    print(prosek)
    exit()
if len(prosek)<=4:
    prosek=prosek+"00"
    print(prosek[0]+prosek[1]+prosek[2]+prosek[3])
    exit()
print(truncate(float(prosek),2))