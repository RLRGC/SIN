# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:31:49 2023

@author: le_rouzr
"""

biblio = [] #liste

biblio.append({
    "auteur":"Baudelaire", 
    "titre": "Fleur du mal", 
    "annee": 1857
}) #Exemple d'ajout de livre



def Ajouter ():
        auteur = input("qui est l'auteur du livre? "),
        titre  = input("quel est le titre du livre? "),
        annee  = int(input("quel est l'année de publication du livre? "))
         
        biblio.append({
            "auteur" : auteur ,
            "titre"  : titre ,
            "annee"  : annee
        })

def Modifier ():
        Livre_A_Modifier = int(input('Quel livre voulez vous Modifier? (ne peut être q un nombre) '))
        
        auteur = input("qui est l'auteur du livre? ")
        titre  = input("quel est le titre du livre? ")
        annee  = int(input("quel est l'année de publication du livre? "))
        
        biblio[Livre_A_Modifier-1] = {
            "auteur" : auteur ,
            "titre"  : titre ,
            "annee"  : annee
        }
def Afficher ():
    Livre = input("Que voulez vous? (titre,auteur,annee)")
    if Livre == "titre":
        TitreDemander = input("Quelle est le titre rechercher")
        for i in range(len(biblio)) :
            print(biblio[i].get(TitreDemander))
            
    if Livre == "auteur":
        AuteurUtilisateur = input("Qui est l'auteur rechercher")
        for i in range(len(biblio)) :
            if biblio[i].get("auteur")==AuteurUtilisateur:
                print(biblio[i].get("titre"))
            
    if Livre == "annee":
        anneeUtilisateur = int(input("Quelle année de publication?"))
        for i in range(len(biblio)) :
            print(biblio[i].get(anneeUtilisateur))
            

#CODE PRINCIPAL
for i in range (10):
    souhaitUtilisateur = input("Que souhaitez vous faire ? (Ajouter,Modifier,Afficher?) ")
    
    if souhaitUtilisateur == "Ajouter" :

        Ajouter()
        print('Livre ajouter avec succès')
        
    if souhaitUtilisateur == "Modifier":
        
        Modifier()
        print('Livre modifier avec succès')
    
    if souhaitUtilisateur == "Afficher" :
        
        Afficher()
    
    if souhaitUtilisateur == "End":
        break