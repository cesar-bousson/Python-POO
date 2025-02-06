

#Job 4 :

'''
Créer une classe nommée Student qui a comme attributs privés un nom, un
prénom, un numéro d’étudiants et un nombre de crédits par défaut à zéro. La
méthode add_credits permet d’ajouter un nombre de crédits au total de
celui de l’étudiant. Ce mutateur doit s’assurer que la valeur passée en
argument est supérieure à zéro pour garantir l’intégrité de la valeur.
Instancier un objet représentant l’étudiant John Doe qui possède le numéro
d’étudiant 145. Ajoutez-lui des crédits à trois reprises et imprimez son total de
crédits en console.

Pour des mesures de confidentialité, l'établissement ne souhaite pas
divulguer la façon dont elle évalue le niveau de ses étudiants. Pour répondre
à cette problématique, créer une méthode nommée "student_eval" qui sera
privée. 
Cette méthode retourne “Excellent” si le nombre de crédits est égal ou
supérieur à 90, “Très bien” si le nombre est supérieur ou égal à 80, “Bien” si le
nombre est supérieur ou égale à 70, “Passable” si égale ou supérieure à 60 et
“Insuffisant” si inférieur à 60.
Ajouter l’attribut privé nommé level dans le constructeur de la classe Student
qui prend en valeur la méthode student_eval. Créer une méthode
student_info qui écrit en console les informations de l’étudiant (nom,
prénom, identifiant et son niveau).

'''
# -------------------------------------------------------------------------

class Student: 
    
    def __init__(self, name, firstname, student_number):
        self.__credit_amount = 0
        self.__name = name
        self.__firstname = firstname
        self.__student_number = student_number 
        self.__level = self.student_eval()
    
    ''''''    
    def set_add_credits(self, amount):
        self.amount = amount #  for user instance (input)
        if amount > 0 and isinstance(amount, int):
            self.__credit_amount += amount
            return self.__credit_amount
        else: 
            raise ValueError("Mauvaise saisie recommencez")
    
    def get_credit_amount(self):
        return f"John DOE crédits : {self.__credit_amount}"

    def student_eval(self):
        if self.__credit_amount >= 90: 
            return "Excellent"
        elif self.__credit_amount >= 80 and self.__credit_amount < 90:
            return "Très bien"
        elif self.__credit_amount >= 70 and self.__credit_amount < 80:
            return "Bien"
        elif self.__credit_amount >= 60 and self.__credit_amount < 70:
            return "Passable"
        elif self.__credit_amount < 60:
            return "Insuffisant"
    
    def student_info(self):
        return f"Etudiant: {self.__name} {self.__firstname} | Numéro : {self.__student_number} |  Niveau : {self.__level}"
        
''''''''''''
#objet1:
etudiant1 = Student("DOE","John", "145")

amount = int(input("Ajouter argent, donner montant : "))
print(etudiant1.set_add_credits(amount))
amount = int(input("Ajouter argent, donner montant : "))
print(etudiant1.set_add_credits(amount))
amount = int(input("Ajouter argent, donner montant : "))
print(etudiant1.set_add_credits(amount))

print(etudiant1.get_credit_amount())


print(etudiant1.student_info())

''''''''''''
