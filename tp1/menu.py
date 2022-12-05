from composition import *
from plat import *


#---------------menu_principal--------------------
while True:
    print("----- Menu Principal------  ")
    print(" 1: ajouter une   plat en fonction de sa sauce et son complement  ")
    print(" 2: ajouter un    complement  ")

    choix=eval(input(" Entrez votre choix: "))
    print("")
    if(choix == 1):
        print("")
        print("information relative a une recette de plat aliment")
        print("--------------------------------------------------")
        Affichedish()
        id=input("entrez l'identifiant de plat: ")
        nom=input("entrez le nom du plat: ")
        sid=input("entrez l'identifiant de sauce: ")
        snom=input("entrez le nom de la sauce: ")
        scouleur=input("entrez la couleur de la sauce: ")
        cid=input("entrez l'identifiant de complement: ")
        cnom=input("entrez le nom du complement: ")
        ccouleur=input("entrez la couleur du complement: ")
        nature=input("quelle est  la nature de se plat ?: ")
        sa=Sauce(sid,snom,scouleur)
        co=Complement(cid,cnom,ccouleur)
        di=Dish(id,nom,nature,sid,snom,scouleur,cid,cnom,ccouleur)
        sa.Ajoutesauce()
        co.AjouteComplement()
        di.AjouteDish()
    elif(choix==2):
        break
