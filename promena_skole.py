import math
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
prosek=round(proseknepodeljen/(predmeta_iz_med_skole-neracunajuci_predmeti),2)

print(prosek)