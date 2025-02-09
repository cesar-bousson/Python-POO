

#Job 2

'''
À l’aide de la classe Personne, Eleve et Professeur créent au-dessus, faites
dire bonjour à votre élève grâce à la méthode bonjour ainsi que “Je vais en
cours” grâce à la méthode allerEnCours. Redéfinir l'âge de l’élève à 15 ans.

Créez un objet Professeur, 40 ans, faites dire bonjour à votre professeur et
commencez le cours grâce à la méthode enseigner.

'''

class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        return f"J'ai {self.age} ans."

    def bonjour(self):
        return "Hello ! \n"

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
        return self.age


class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        return "Je vais en cours."

    def afficherAge(self):
        return f"j'ai {self.age} ans.\n"
    
class Professeur(Personne): 
    def __init__(self, matiere,):
        super().__init__()
        self.__matiere = matiere

    def enseigner(self):
        return f"Le cours de {self.__matiere} va commencer.\n"

eleve1 = Eleve()

'''exo 2.1 '''
eleve1.modifierAge(15) #modifie l'age

print(eleve1.bonjour())
print(eleve1.allerEnCours())
print(eleve1.afficherAge())

'''exo 2.2 '''
prof1 = Professeur("Math")
prof1.modifierAge(40)

print(prof1.bonjour())
print(prof1.afficherAge())
print(prof1.enseigner())