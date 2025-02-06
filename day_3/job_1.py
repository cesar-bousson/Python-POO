
# Job 1:
'''
Créer une classe Ville avec comme attributs privés un nom et un nombre
d'habitants.
Créer une classe Personne avec les attributs privés suivants : nom, âge et un
objet de la classe ville.
Ajouter la méthode ajouterPopulation dans la classe Personne qui permet
d’augmenter de 1 le nombre d’habitants de la ville.

Créer un objet Ville avec comme arguments “Paris” et 1000000.
Afficher en console le nombre d’habitants de la ville de Paris.

Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
Afficher en console le nombre d’habitants de la ville de Marseille.

Créer les objets suivants :
- John, 45 ans, habitant à Paris
- Myrtille, 4 ans, habitant à Paris.
- Chloé, 18 ans, habitant à Marseille.

Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces
nouvelles personnes.

(voir cours sur objets mutables / passage par réference)
'''

# ------------------------------------------------



class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def ajouter_habitant(self):
        self.__nb_habitants += 1

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouter_population()

    def ajouter_population(self):
        self.__ville.ajouter_habitant()



paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"Nombre d'habitants à {paris.get_nom()} : {paris.get_nb_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()} : {marseille.get_nb_habitants()}")


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


print(f"Nombre d'habitants à {paris.get_nom()} après l'arrivée de nouvelles personnes : {paris.get_nb_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()} après l'arrivée de nouvelles personnes : {marseille.get_nb_habitants()}")
