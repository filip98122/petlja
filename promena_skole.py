predmeta_iz_med_skole = int(input())
neracunajuci_predmeti = int(input())
l = []
for i in range(neracunajuci_predmeti):
    ocena_za_taj_predmet = int(input())
    l.append(ocena_za_taj_predmet)
prosek = float(input())
prosek*=predmeta_iz_med_skole
for i in range(neracunajuci_predmeti):
    prosek-=l[i]
print('{0:.2f}'.format(prosek/(predmeta_iz_med_skole-neracunajuci_predmeti)))