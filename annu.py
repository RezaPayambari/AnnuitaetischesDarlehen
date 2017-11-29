from decimal import *
import math

def is_number(s):
    try:
        Decimal(s)
        return True
    except ValueError:
        return False

darlehen = Decimal(0)
zinssatz = Decimal(0)
laufzeit = Decimal(0)
annuitaet= Decimal(0)

while Decimal(darlehen)<=0:
    darlehen = input("Geben Sie bitte die Darlehen ein: (€) ")
    if darlehen.isdigit():
        darlehen=Decimal(darlehen)
    else:
        print("please enter a number")
        darlehen=0


while Decimal(zinssatz)<=0:
    zinssatz = input("Geben Sie bitte die Zinssatz ein: (%) ")
    if zinssatz.isdigit():
        zinssatz=Decimal(zinssatz)
    else:
        print("please enter a number")
        zinssatz=0


while Decimal(laufzeit) <= 0:
    laufzeit = input("Geben Sie bitte die Laufzeit ein: (Jahr) ")
    if laufzeit.isdigit():
        laufzeit=Decimal(laufzeit)
    else:
        print("please enter a number")
        laufzeit=0


annuitaet= darlehen * (
    (((1+(zinssatz/100))**laufzeit)*(zinssatz/100))
    /
    (((1+(zinssatz/100))**laufzeit)-1)
)


print("Annuität : ",'%.2f' % annuitaet)

print()
print("================================================================================")
print()
tmpZeit=1

zinsanteil1 = darlehen * (zinssatz / 100)
tilgungsanteil1 = annuitaet - zinsanteil1


while tmpZeit<=laufzeit:
    tilgungsanteil= tilgungsanteil1 * ((1+(zinssatz / 100))**(tmpZeit-1))
    zinsanteil=  annuitaet - tilgungsanteil
    print("Aktuelles%  Jahr ",'%.0f'% tmpZeit)
    print()
    print("Zinsanteil : ",'%.2f'% zinsanteil , "          ","tilgungsanteil : ",'%.2f' % tilgungsanteil)
    print()
    print("================================================================================")
    print()
    tmpZeit +=1

print("Gesamter Betrag : ",'%.2f' % (annuitaet*laufzeit))