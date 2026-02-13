import math
predmeta_iz_med_skole = int(input())
neracunajuci_predmeti = int(input())
l = []
for i in range(neracunajuci_predmeti):
    ocena_za_taj_predmet = int(input())
    l.append(ocena_za_taj_predmet)
prosek = float(input())
proseknepodeljen=prosek*predmeta_iz_med_skole
for i in range(neracunajuci_predmeti):
    proseknepodeljen-=l[i]
prosek=proseknepodeljen/(predmeta_iz_med_skole-neracunajuci_predmeti)
p=str(prosek)+"000"
print(p[0]+p[1]+p[2]+p[3])