#Job 6

'''
Créer une classe Vehicule avec comme attribut une marque, le modèle, une
année et un prix. Créer la méthode informationsVehicule qui écrit en console
la marque, le modèle, l'année et le prix du véhicule.

Créer la classe Voiture qui hérite de la classe Vehicule. Dans le constructeur
de la classe Voiture, ajouter un attribut portes qui contient le nombre entier 4.
Créer dans cette classe, une méthode informationsVehicule qui affiche, en
console, les informations générales du véhicule et le nombre de portes de la
voiture.

Instancier un objet Voiture, passer les informations dont la classe a besoin et
faites appel à la méthode informationsVehicule.

Créer une classe Moto qui hérite de la classe Vehicule et ajouter l'attribut
roue qui contient par défaut l’entier 2. Créer à nouveau une méthode
informationsVehicule dans la classe Moto qui affiche l'intégralité des
informations de la moto.
Instancier un objet Moto et faites appel à la méthode informationsVehicule.

Créer la méthode demarrer dans la classe Véhicule qui écrit en console
“Attention, je roule”. Surcharger la méthode demarrer dans la classe Moto et
Voiture afin d’afficher un message personnalisé. Faites démarrer votre
voiture et votre moto.

'''

class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print("La voiture démarre : vroom vroom !")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print("La moto démarre : braaap braaap !")


#objets
voiture = Voiture("Toyota", "Corolla", 2023, 25000)
moto = Moto("Yamaha", "MT-07", 2022, 8000)

# Appel méthodes informationsVehicule
print("Informations de la voiture :")
voiture.informationsVehicule()

print("\nInformations de la moto :")
moto.informationsVehicule()

# Appel méthodes demarrer
print("\nDémarrage de la voiture :")
voiture.demarrer()

print("\nDémarrage de la moto :")
moto.demarrer()
