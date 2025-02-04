
#job 8 :

'''
Créez la classe “Cercle” recevant en argument son rayon, également initialisé
dans le constructeur.
Ajoutez les méthodes suivantes :
- changerRayon qui permet de modifier le rayon.
- afficherInfos qui permet d’afficher toutes les informations du cercle.
- circonférence qui permet de retourner la circonférence.
- aire qui permet de retourner l’aire du cercle.
- diametre qui permet de retourner le diamètre du cercle.

Créez deux cercles avec comme rayon 4 et 7. Pour chaque cercle, affichez ses
informations, affichez sa circonférence, son diamètre et son aire.
'''

class Cercle: 
    def __init__(self, rayon):
        self.rayon = rayon
        self.circonférence1 = 0
        self.diametre1 = 0
        self.pi = 3.14159
        self.aire1 = 0
        
    def changerRayon(self):
        self.rayon = int(input("Choisir nouveau rayon: "))
        return f"Le nouveau rayon est : {self.rayon}"
        
    def circonférence(self):
        self.circonférence1 = (2*self.pi*self.rayon) # C = 2 x Pi x R
        return f"\nCirconférence : {self.circonférence1}"
        
    def aire(self):
        self.aire1 = (self.pi*self.rayon**2) # Aire = pi x rayon²
        return f"\n Aire : {self.aire1}"
    
    def diametre(self):
        self.diametre1 = self.rayon*2 # Diametre = Rx2
        return f"\n Diamètre : {self.diametre1}"
    
    def afficherInfos(self):
        return f" \n Informations du cercle : \n Rayon : {self.rayon} , Circonférence: {self.circonférence1}, Diamètre : {self.diametre1} \n"
    
     
cercle1 = Cercle(4) 
cercle2 = Cercle(7) 

print (cercle1.changerRayon())
print (cercle2.changerRayon())

print(cercle1.circonférence())
print(cercle2.circonférence())

print(cercle1.aire())
print(cercle2.aire())

print(cercle1.diametre())
print(cercle2.diametre())

print(cercle1.afficherInfos())
print(cercle2.afficherInfos())
