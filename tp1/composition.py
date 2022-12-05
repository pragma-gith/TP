

class Sauce :
    """constructeur de l'objet sauce"""
    def __init__(self,sid,snom,scouleur):
        self.sid=sid
        self.snom=snom
        self.scouleur=scouleur
    """methode de recuperation d'un attribut"""
    def geTsid(self):
        return self.sid
    
    def geTsNom(self):
        return self.snom
    
    def geTsCouleur(self):
        return self.scouleur

    def Ajoutesauce(self):
        f1=open("sauce.txt","a+")
        f1.write(self.geTsid() + "\t" +  self.geTsNom() + "\t" + self.geTsCouleur() + "\n")
        f1.close()
def Affichesauce():
    ligne=[]#creation d'une liste vide
    print("\nid \t nom  \tcouleur")
    f1=open("sauce.txt","r")
    for li in f1:
        print(li)
    f1.close()


class Complement :
    """constructeur de l'objet complement"""
    def __init__(self,cid,cnom,ccouleur):
        self.cid=cid
        self.cnom=cnom
        self.ccouleur=ccouleur
    """methode de recuperation d'un attribut"""
    def geTcid(self):
        return self.cid
    
    def geTcNom(self):
        return self.cnom
    
    def geTcCouleur(self):
        return self.ccouleur
    
    def AjouteComplement(self):
        f2=open("complement.txt","a+")
        f2.write(self.geTcid() + "\t" +  self.geTcNom() + "\t" + self.geTcCouleur() + "\n")
        f2.close()
        
def AffichauceComplement():
    ligne=[]#creation d'une liste vide
    print("\nid \t nom  \tcouleur")
    f2=open("complement.txt","r")
    for li in f2:
        print(li)
    f2.close()
