

# Job 4

'''
Créer une classe pour représenter un joueur ainsi qu'une classe pour
représenter une équipe de foot.

La classe Joueur doit avoir les attributs suivants : nom, numéro, position,
nombre de buts marqués, passes décisives effectuées, cartons jaunes reçus
et cartons rouges reçus. Tous ces attributs doivent être initialisés lors de la
création de l’objet Joueur.

Cette classe doit posséder les méthodes suivantes :
➔ marquerUnBut,
➔ effectuerUnePasseDecisive,
➔ recevoirUnCartonJaune,
➔ recevoirUnCartonRouge,
➔ afficherStatistiques.

Ces méthodes permettent de mettre à jour les statistiques du joueur.

La classe Equipe doit avoir les attributs nom et liste de joueurs. Le nom de
l’équipe et la liste de joueurs (liste vide par défaut) doivent être initialisés
dans le constructeur.

Ajouter les méthodes suivantes dans la classe Equipe :
- ajouterJoueur : cette méthode ajoute un joueur à l’équipe.
- AfficherStatistiquesJoueurs : cette méthode permet d’afficher toutes
les statistiques de l’ensemble des joueurs.
- mettreAJourStatistiquesJoueur : cette méthode permet de mettre à
jour les statistiques d’un joueur (buts, cartons ...).

Créez plusieurs joueurs avec les paramètres de votre choix et ajoutez-les aux
équipes.

Présenter l’ensemble des joueurs de chaque équipe. Utiliser les différentes
méthodes afin de simuler un match, marquer un but, avoir un carton rouge...
Et afficher à nouveau les statistiques des joueurs.

'''

class Joueur:
    def __init__(self, nom, numero, position, buts, passes, jaunes, rouges):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        return (f"Nom: {self.nom}, Numéro: {self.numero}, Position: {self.position}, "
                f"Buts: {self.buts}, Passes: {self.passes}, Cartons Jaunes: {self.jaunes}, "
                f"Cartons Rouges: {self.rouges}")


class Equipe:
    def __init__(self, nom, joueurs=None):
        self.nom = nom
        self.joueurs = joueurs if joueurs else []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self, numero, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.joueurs:
            if joueur.numero == numero:
                joueur.buts += buts
                joueur.passes += passes
                joueur.jaunes += jaunes
                joueur.rouges += rouges
                break

# Création des joueurs
joueur1 = Joueur("Lionel Messi", 10, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Sergio Ramos", 4, "Défenseur", 0, 0, 0, 0)
joueur3 = Joueur("Kylian Mbappé", 7, "Attaquant", 0, 0, 0, 0)

# Création d'équipe
psg = Equipe("Paris Saint-Germain")

# Ajout des joueurs à l'équipe
psg.ajouterJoueur(joueur1)
psg.ajouterJoueur(joueur2)
psg.ajouterJoueur(joueur3)

# Affichage des statistiques initiales
print("Statistiques initiales des joueurs :")
psg.afficherStatistiquesJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.marquerUnBut()
joueur3.recevoirUnCartonRouge()

# Affichage des statistiques après le match
print("\nStatistiques après le match :")
psg.afficherStatistiquesJoueurs()

