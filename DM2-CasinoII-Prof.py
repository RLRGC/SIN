from random import randint 

# QUESTION 11
def TirerRetirerCartePacket(Packet):
    """Prend une carte aléatoirement dans un packet, renvoie la carte et le packet actualisé."""
    card = list(Packet)[randint(0,len(list(Packet))-1)]
    Packet.pop(card)
    return card, Packet

# QUESTION 12
def DictionaireCartes(Joker=False):
    """Renvoie un dictionnaire de cartes sous forme de liste où chaque emoji carte est associé à sa valeur numérique."""
    cartes=[chr(x) for x in range(0x1F0A1, 0x1F0AF)] # Liste des cartes
    Packet={cartes[i]:i+1 for i in range(len(cartes))} # Dictionaire carte:valeur.
    if Joker:
        Packet.update({"🃏" : 15}) # On peut rajouter True à l'appel de fonction pour rajouter un joker
    return Packet

# QUESTION 13
def Tour(Packet):
    """Joue un tour de la partie en retirant deux cartes du packet (Une pour joueur et une pour ordi)."""
    CarteJoueur=TirerRetirerCartePacket(Packet)
    CarteOrdi=TirerRetirerCartePacket(CarteJoueur[1])
    return CarteOrdi[1], CarteJoueur[0], CarteOrdi[0] # Renvoie le pakcet actualisé, la carte joueur et la carte ordi

def SommeMain(liste, Ref):
    """Calcule la somme d'une main (Liste de cartes). Prend en arguments une liste et le dictionnaire de référence où sont stockées les valeurs des cartes."""
    x=0
    for i in liste:
        x+=Ref[i]
    return x

def Compare():
    """Demande à l'utilisateur un signe de comparaison + - =."""
    while True:
        c=input("Tapez [+] [-] ou [=] : ")
        if c in ["+", "-", "="]:
            break
        else:
            print("Ce n'est pas un signe (+/-/=)\n---")
    return c

def JoueurGagne(joueur, ordi, r, comparaisonsymbole):
    """La condition est trop longue donc on la met là. Elle renvoie un booléen si le joueur a le bon signe de comparaison entre les mains."""
    # joueur, ordi : Listes des cartes des deux adversaires (mains)
    # r : Dictionnaire de référence dans lequel les valeurs des cartes sont associées aux cartes présentes dans les listes
    return (SommeMain(joueur, r)>SommeMain(ordi, r) and comparaisonsymbole=="+") or (SommeMain(joueur, r)<SommeMain(ordi, r) and comparaisonsymbole=="-") or (SommeMain(joueur, r)==SommeMain(ordi, r) and comparaisonsymbole=="=")

def Miser():
    """Demande à l'utilisateur un nombre pour miser l'argent de départ."""
    while True:
        try:
            MiseIn=float(input("Mise="))
            if MiseIn%1==0:
                MiseIn=int(MiseIn)
            break
        except ValueError:
            print("C'est pas un nombre")
    return MiseIn

def AfficherMain(Listemain):
    texte=""
    for i in Listemain:
        texte+=str(i)+" "
    return texte[:-1] # on enlève le dernier espace avec du saucissonnage slicing

def main(Joker):
    """Fonction principale. Prend en arguments un booléen si on veut rajouter une carte Joker de valeur 15."""
    Ref=DictionaireCartes(Joker) # Dictionnaire de référence qui ne change pas
    Cartes=DictionaireCartes(Joker) # Dictionnaire de jeu qui se vide au fur et à mesure du jeu
    
    MiseDepart=Miser() # On pourra ainsi comparer le bénéfice d'argent à la fin avec deux variables (une qui changera et une fixe)
    Mise=MiseDepart
    
    # Initialisation Variables Globales
    i=0
    CartesJoueur=[] # Main du Joueur
    CartesOrdi=[]   # Main de l'Ordi
    PartieEnCours=True
    while len(Cartes)>=2 and PartieEnCours:
        """On joue tant que le joueur veut jouer et qu'il reste des cartes."""
        i+=1
        print(f"▬▬▬▬▬▬▬▬▬ Tour {i} ▬▬▬▬▬▬▬▬▬")
        # Le joueur et l'ordinateur prennent une carte
        tour=Tour(Cartes)
        Cartes=tour[0]
        CartesJoueur.append(tour[1])
        CartesOrdi.append(tour[2])
    
        print(f"Votre main : {AfficherMain(CartesJoueur)} ({SommeMain(CartesJoueur, Ref)})")
        comparaison=Compare() # Demande le Signe de comparaison à l'utilisateur
        print(f"Votre main : {AfficherMain(CartesJoueur)} ({SommeMain(CartesJoueur, Ref)})\nMain ordinateur: {AfficherMain(CartesOrdi)} ({SommeMain(CartesOrdi, Ref)})")
        
        if JoueurGagne(CartesJoueur, CartesOrdi, Ref, comparaison):
            print("VOUS AVEZ GAGNÉ")
            Mise*=2
            PartieEnCours=input(f"Continuer ? Vous avez actuellement {Mise}€ (Oui/Non)") in ["Oui", "oui", "O", "o"]
        else:
            print("VOUS AVEZ PERDU")
            PartieEnCours=False
            Mise=0
    print(f"Vous avez {Mise}€, ce qui vous fait un bénéfice de {Mise-MiseDepart}€")
main(Joker=True)