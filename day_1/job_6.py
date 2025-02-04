
# Job 6

'''
Créez une classe Animal avec un attribut age initialisé à zéro et prenom
initialisé vide dans son constructeur.
Instanciez un objet Animal et affichez en console l’attribut âge. Créez une
méthode vieillir qui ajoute 1 à l'âge de l’animal. Faites vieillir votre animal et
affichez son âge mis à jour en console.

Créez une méthode nommer qui prend en paramètre le nom de l’animal.
Nommez votre animal et affichez en console son nom.

'''

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
        return self.age
    
    def nommer(self):
        self.type = "lion"
        return f"{self.type}"
    
animal1 = Animal()

print(f"\n Age actuel : {animal1.age} ans. \n")

print (f"\n Nouvel age dans un an: {animal1.vieillir()} ans. \n")

print(f"\n Cet animal est un : {animal1.nommer()} \n")