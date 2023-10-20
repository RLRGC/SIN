from random import randint 

def trait ():
    print("--------------------")
    return None
def jeu():

    nb_ordi = randint(0,50)

    Nbs_Essais = 0 


    while True :

        UserNumber = int(input("Choisi un nombre : "))
        if UserNumber > 50 or UserNumber < 0 :
            trait()
            print("Aucune chance, c'est pas dans l'intervalle.")
            trait()
        if UserNumber < nb_ordi : 
            trait()
            print("Vous êtes en dessous! ")
            trait()
            Nbs_Essais+=1
        if UserNumber > nb_ordi :
            trait()
            print("Vous êtes au dessus!  ")
            trait()
            Nbs_Essais+=1
        if UserNumber == nb_ordi : 
            trait()
            print("Vous avez gagné ! Cela vous a pris {} essais".format(Nbs_Essais))
            trait()
            break

jeu()
jouer = 0
while True: 
    answer = input("Voulez vous rejouer? ")
    if answer == "Oui" or answer == "oui":
        jouer+=1
        jeu()
    else:
      print("Merci d'avoir joué {} fois".format(jouer))
      break 