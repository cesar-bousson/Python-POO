
#job 9 :

''' Créez la classe Produit avec des attributs nom, prixHT, TVA. Implémentez la
méthode CalculerPrixTTC qui retourne le prix produit avec la TVA. Ajoutez la
méthode afficher qui liste l’ensemble des informations du produit.
Créez plusieurs produits et calculez leurs TVA.

Ajoutez des méthodes permettant de modifier le nom du produit et son prix.
Ainsi que des méthodes permettant de retourner chaque information du
produit.
Modifiez le nom et le prix de chaque produit et affichez en console le nouveau
prix des produits.

La fonction print() ne doit pas être utilisée dans la classe Produit.
Sur vos scripts doit apparaître l’ensemble des méthodes appelées tout au
long des exercices. '''

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        self.prixTTC = 0
        
    def calculerPrixTTC(self): # TTC = prixHT x (1+ tva/100)
        self.prixTTC = (self.prixHT*(1+self.TVA))
        return f" \n Prix TTC :  {self.prixTTC}€ \n"
    
    def afficher(self): 
        return f"\n Informations produit : \nNom : {self.nom}, \nPrix HT : {self.prixHT}€, \nTVA : {self.TVA*100}%, \n Prix TTC: {self.prixTTC}€ \n"

    def modifier_nom(self):
        self.nom = input(" Nouveau nom de produit: ")
        return
    def modifier_prix(self):
        self.prixHT = float(input(" Nouveau prix du produit: "))
        return
    
    #retourner les infosau cas par cas :
    def retourner_prixHT(self):
        return self.prixHT
    def retourner_nom(self):
        return self.nom
    def retourner_TVA(self):
        return self.TVA
    def retourner_prixTTC(self):
        self.prixTTC = (self.prixHT*(1+self.TVA))
        return self.prixTTC
        
        
    
produit1 = Produit("Fromage", 15.0, 0.2)   


print(produit1.calculerPrixTTC())
print(produit1.afficher())
print(produit1.modifier_nom())
print(produit1.modifier_prix())
print(produit1.retourner_nom())
print(produit1.retourner_prixHT())
print(produit1.retourner_TVA())
print(produit1.retourner_prixTTC())

