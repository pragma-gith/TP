from composition import *
class Dish :
    """constructeur de l'objet dish"""
    """relation de composition"""
    """plat ----> sauce &&  plat ----> complement"""
    def __init__(self,id,nom,nature,sid,snom,scouleur,cid,cnom,ccouleur):
        self.id=id
        self.nom=nom
        self.nature=nature
        self.sauce=Sauce(sid,snom,scouleur)
        self.complement=Complement(cid,cnom,ccouleur)
    """methode de recuperation d'un attribut"""
    def geTid(self):
        return self.id
    
    def geTNom(self):
        return self.nom
    
    def geTSAuce(self):
        return self.sauce
    
    def geTComplement(self):
        return self.complement
    
    def geTNature(self):
        return self.nature

    def AjouteDish(self):
        f2=open("dish.txt","a+")
        f2.write(self.geTid() +"\t"+ self.geTNom() +"\t"+ self.geTNature()+"\t"+ self.geTSAuce().geTsid()+"\t"+ self.geTSAuce().geTsNom()+"\t" + self.geTSAuce().geTsCouleur()+"\t"+self.geTComplement().geTcid()+"\t"+ self.geTComplement().geTcNom()+"\t" + self.geTComplement().geTcCouleur()+"\n")
        f2.close()
    
def Affichedish():
    f2=open("dish.txt","r")
    print("iD\tPLAT\tNATURE  \tsiD\tSAUCE\tCouleur\tciD\tCOMPLEMENT\tcouleur")
    for li in f2.readlines():
        print(li,end=" ")
    f2.close()


def Affichedishe():
    f2=open("dish.txt","r")
    nom=input("quelle nom de plat voulez vous consulter les informations?: ")
    
    print("iD\tPLAT\tNATURE  \tsiD\tSAUCE\tCouleur\tciD\tCOMPLEMENT\tcouleur")
    for ligne in f2.readlines():
        for i in ligne:
            if ligne==nom:
               print(ligne[i])
    f2.close()














    
