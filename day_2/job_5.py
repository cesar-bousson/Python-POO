

#Job 5
'''
Créer une classe Voiture qui a pour attributs privés une marque, un modèle,
une année, un kilométrage et un attribut nommé en_marche initialisé par
défaut à False.
Cette classe doit posséder des mutateurs(setter) et accesseurs(getter) pour chaque attribut.

Créer une méthode demarrer qui change la valeur de l’attribut en_marche
en True, une méthode arreter qui change la valeur de l’attribut en_marche
en False.

Ajouter à la classe Voiture l’attribut privé reservoir qui est initialisé à 50 par
défaut dans le constructeur. Créer une méthode privée verifier_plein qui
retourne la valeur de l’attribut reservoir. Cette méthode est appelée dans la
méthode demarrer. Si la valeur du réservoir est supérieure à 5 la voiture peut
démarrer.

'''

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        
        self.en_marche = False
        self.__reservoir = 50
        
    # --------------------
    def get_marque(self):
        return self.__marque
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque # à instancier
    ''''''''    
    def get_modele(self):
        return self.__modele
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele # à instancier
    ''''''''
    def get_annee(self):
        return self.__annee
    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee # à instancier
    ''''''''
    def get_kilometrage(self):
        return self.__kilometrage
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage # à instancier

    ''''''''
    def __verifier_plein(self):
        return self.__reservoir
    
    def demarrer(self):
        self.__verifier_plein()
        if self.__verifier_plein() > 5:
            self.en_marche = True
            return "La voiture eut démarrer"
        else:
            return "Faites le plein pour demarrer"
    
    def arreter(self):
        self.en_marche = False
        return "Voiture arrété"
        
    ''''''''
        
#objet :    
voiture1 = Voiture("Porsche", "Cayen", 1993, 13000)

#setters :
nouvelle_marque = input(" Nouvelle marque : ")
nouveau_modele = input(" Nouveau modele : ")
nouvelle_annee = input(" Nouvelle année : ")
nouveau_kilometrage = input(" Nouveau kilométrage : ")
