from random import *


piques = range(0x1F0A1, 0x1F0AF)

cartes = [chr(x) for x in piques]
CarteUtilisateur = 0

#fonction permettant de tirer une carte du paquet, retirer la carte et renvoyer la carte et le paquet mis à jour
def Pioche():
    
   shuffle(cartes)
   CarteUtilisateur = cartes[0]
   cartes.remove(CarteUtilisateur)

def PiocheOrdinateur():
    
    shuffle(cartes)
    CartesOrdinateur = cartes[0]
    cartes.remove(CartesOrdinateur)


DicCartes = {}

for i in range(1,14):
    DicCartes[i]=cartes[i-1]

def MainJoueur ():
    shuffle(cartes)
    pioche=cartes[0]
    cartes.remove(pioche)
    if DicCartes[1] == pioche :
        return DicCartes[1]
    if DicCartes[2] == pioche :
        return DicCartes[2]
    if DicCartes[3] == pioche :
        return DicCartes[3]
    if DicCartes[4] == pioche :
        return DicCartes[4]
    if DicCartes[5] == pioche :
        return DicCartes[5]
    if DicCartes[6] == pioche :
        return DicCartes[6]
    if DicCartes[7] == pioche :
        return DicCartes[7]
    if DicCartes[8] == pioche :
        return DicCartes[8]
    if DicCartes[9] == pioche :
        return DicCartes[9]
    if DicCartes[10] == pioche :
        return DicCartes[10]
    if DicCartes[11] == pioche :
        return DicCartes[11]
    if DicCartes[12] == pioche :
        return DicCartes[12]
    if DicCartes[13] == pioche :
        return DicCartes[13]

MainJoueur()