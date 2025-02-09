
#Jour 4 : L’héritage
'''
La programmation, c’est Class

C’est juste une histoire de famille...
L'héritage permet de construire une classe B à partir d’une classe A. Il permet
de définir un lien de parenté entre deux classes. Ces deux classes partagent
donc de nombreuses choses, leurs attributs, méthodes, etc.
'''

# Job 1
'''
Créer une classe Personne qui aura comme attribut age prenant un entier et
initialisé à 14 par défaut. Ajouter une méthode afficherAge qui affichera en
console l'âge de la personne et une méthode bonjour qui écrit en console
‘Hello’. Créer une méthode modifierAge prenant en paramètre un entier et
permettant de modifier l'âge de la personne.

Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut
et une méthode publique allerEnCours qui affiche : “Je vais en cours” ainsi
qu’une méthode afficherAge qui écrit en console : “J’ai XX ans”.
Créer une classe Professeur avec un attribut privé matiereEnseignee, qui
indiquera la matière du professeur, et une méthode publique enseigner qui
affiche : “Le cours va commencer”.

Instancier une classe Personne et une classe Eleve. Afficher l'âge par défaut
de l’élève en console.

'''

class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        return self.age

    def bonjour(self):
        return "Hello"

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        return "Je vais en cours"

    def afficherAge(self):
        return f"j'ai {self.age} ans"
    
class Professeur: 
    def __init__(self, matiere):
        self.__matiere = matiere

    def enseigner(self):
        return "Le cours va commencer."

eleve1 = Eleve()

'''exo 1'''
print(eleve1.afficherAge())


#--------------------------
