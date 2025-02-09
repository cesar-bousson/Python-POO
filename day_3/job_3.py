

#Job 3
'''
Dans cet exercice, vous allez créer votre to do list.

Créer une classe Tache qui représente une tâche à faire. Cette classe a
comme attribut un titre, une description et un statut (à faire ou terminer)
initialisés dans le constructeur.

Créer une classe ListeDeTaches qui représente la liste des tâches à faire ainsi
que toutes les méthodes nécessaires à la gestion de celles-ci avec comme
attribut taches(liste).

Ajouter les méthodes suivantes :
➔ ajouterTache : qui permet d’ajouter une tâche.
➔ supprimerTache : qui permet de supprimer une tâche.
➔ marquerCommeFinie : qui permet de signaler que la tâche est faite.
➔ afficherListe : qui permet de retourner une liste de toutes les tâches.
➔ filterListe : qui permet de filtrer les tâches par rapport à un statut et
retourne cette liste.

Tester votre code en créant plusieurs instances de Tache, les ajouter à la
classe listeDeTache, supprimer une tache, changer le statut d’une tâche,
afficher toutes les tâches et afficher les tâches à faire.

'''

class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self._titre = titre
        self._description = description
        self._enregistrer = False
        self._statut = statut if statut in ["à faire", "terminé"] else "à faire"

    def changer_statut(self, nouveau_statut):
        """Change le statut de la tâche et met à jour l'état d'enregistrement."""
        if nouveau_statut in ["à faire", "terminé"]:
            self._statut = nouveau_statut
            self._enregistrer = nouveau_statut == "terminé"
        else:
            raise ValueError("Statut invalide. Utilisez 'à faire' ou 'terminé'.")

    def __str__(self):
        return f"Titre: {self._titre}, Description: {self._description}, Statut: {self._statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache: Tache):
        """Ajoute une tâche à la liste."""
        if isinstance(tache, Tache):
            self.taches.append(tache)
        else:
            raise TypeError("Seuls les objets de type 'Tache' peuvent être ajoutés.")

    def lister_taches(self):
        """Retourne la liste des tâches sous forme de chaîne."""
        return [str(tache) for tache in self.taches]

    def taches_terminees(self):
        """Retourne la liste des tâches terminées."""
        return [tache for tache in self.taches if tache._statut == "terminé"]


# Exemple d'utilisation
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Sport", "Aller courir 5km", "terminé")
tache3 = Tache("Lecture", "Lire un chapitre de mon livre")

liste1 = ListeDeTaches()
liste1.ajouter_tache(tache1)
liste1.ajouter_tache(tache2)
liste1.ajouter_tache(tache3)

print("Toutes les tâches :")
print("\n".join(liste1.lister_taches()))

print("\nTâches terminées :")
print("\n".join(str(tache) for tache in liste1.taches_terminees()))



# -------------------------------------------------CORRECTION --------------------------------------------

'''
class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"

    def afficherListe(self):
        return [str(tache) for tache in self.taches]

    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

# Tests
def main():
    # Créer une liste de tâches
    liste = ListeDeTaches()

    # Ajouter des tâches
    t1 = Tache("Faire les courses", "Acheter des fruits et légumes")
    t2 = Tache("Ranger la maison", "Nettoyer le salon et la cuisine")
    t3 = Tache("Préparer le repas", "Préparer le dîner pour ce soir")

    liste.ajouterTache(t1)
    liste.ajouterTache(t2)
    liste.ajouterTache(t3)

    # Afficher toutes les tâches
    print("\nToutes les tâches:")
    print("\n".join(liste.afficherListe()))

    # Marquer une tâche comme finie
    liste.marquerCommeFinie("Faire les courses")

    # Afficher les tâches après modification
    print("\nAprès avoir marqué 'Faire les courses' comme terminée:")
    print("\n".join(liste.afficherListe()))

    # Filtrer les tâches à faire
    print("\nTâches à faire:")
    print("\n".join(liste.filterListe("\u00e0 faire")))

    # Supprimer une tâche
    liste.supprimerTache("Ranger la maison")

    # Afficher les tâches après suppression
    print("\nAprès avoir supprimé 'Ranger la maison':")
    print("\n".join(liste.afficherListe()))

if __name__ == "__main__":
    main()
'''