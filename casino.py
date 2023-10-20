from random import randint 

def clearConsole():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def trait():
    """Utilité 0 c'est juste de la déco"""
    print("----------------------------")

def TirerRetirerCartePacket(Packet): # QUESTION 11
    card = list(Packet)[randint(0,len(list(Packet))-1)]
    Packet.pop(card)
    return card, Packet

def DictionaireCartes(Joker=False): # QUESTION 12
    Packet={}
    catégories=[" de pique", " de trèfle", " de coeur", " de carreau"]
    for c in catégories:
        Packet.update(dict([[str(i)+c,i] for i in range(2,11)]+[["Vallet"+c,11], ["Dame"+c,12], ["Roi"+c,13], ["As"+c,14]]))
    if Joker:
        Packet.update({"🃏A" : 15, "🃏B" : 15})
    return Packet

def Tour(Packet): # QUESTION 13
    CarteJoueur=TirerRetirerCartePacket(Packet)
    CarteOrdi=TirerRetirerCartePacket(CarteJoueur[1])
    return CarteOrdi[1], CarteJoueur[0], CarteOrdi[0]

def main(Joker):
    Ref=DictionaireCartes(Joker)
    Cartes=DictionaireCartes(Joker)
    while True:
        try:
            MiseIn=float(input("Mise="))
            if MiseIn%1==0:
                MiseIn=int(MiseIn)
            break
        except ValueError:
            print("C'est pas un nombre")
    Mise=MiseIn
    PartieEnCours=True
    trait()
    i=0
    while len(Cartes)>=2 and PartieEnCours:
        i+=1
        print(f"▬▬▬▬▬▬▬▬▬ Tour {i} ▬▬▬▬▬▬▬▬▬")
        tour=Tour(Cartes)
        Cartes=tour[0]
        print(f"Votre carte : {tour[1]} ({(Ref[tour[1]])})\nCarte adverse : {tour[2]} ({(Ref[tour[2]])})")
        if Ref[tour[1]]>=Ref[tour[2]]: # Joueur bat ordi
            print("VOUS AVEZ GAGNÉ")
            Mise*=2
            PartieEnCours=input(f"Continuer ? Vous avez actuellement {Mise}€ (True/False)") in ["True", "true", "t", "T"]
        else:
            print("VOUS AVEZ PERDU")
            PartieEnCours=False
            Mise=0
        trait()
    print(f"Vous avez {Mise}€, ce qui vous fait un bénéfice de {Mise-MiseIn}€")

clearConsole() # pour faire joli si t'es sur VS Code
main(Joker=True)

