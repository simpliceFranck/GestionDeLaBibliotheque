import os

MESSAGE_ACCUEIL = "*** BIENVENUE DANS LA BIBLIOTHÈQUE DE LA GARE ***"
MESSAGE_01 = """
Choisissez parmi les treize options suivantes :

00. Charger les données
01. Ajouter un utilisateur(admin ou usager)
02. Ajouter un livre 
03. Supprimer un livre
04. Rechercher un livre
05. Emprunter un livre
06. Retourner un livre
07. Lister les livres
08. Statistiques
09. Lister les utilisateurs
10. Sauvegarder les données
11. Supprimer un utilisateur
12. Mettre à jour un livre
13. Quitter

Attention, pour les options 01, 02, ...09, il faut mettre 1, 2, ....9 ! 

👉 Votre choix : """

MESSAGE_02 = "Veuillez choisir une option parmi les treize proposées."
MESSAGE_03 = "Au revoir et à bientôt !"
MESSAGE_04 = "Nom et prénom (Dupont Martin) : ? "
MESSAGE_05 = "Nom et prénom à supprimer : ? "
MESSAGE_06 = "Nom et prénon de l'opérateur chargé de valider cette opération : ? "
MESSAGE_07 = "Vous n'êtes pas autorisé à effectuer cette opération."
MESSAGE_08 = "Vous n'êtes pas autorisé à valider cette opération."
MESSAGE_09 = "Mot = de passe : ? "
MESSAGE_10 = "Mot de passe invalide !"
MESSAGE_11 = "Vous êtes inconnus !"

DOSSIER_COURANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_DATA = os.path.join(DOSSIER_COURANT, "Data")
CHOIX_POSSIBLES = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"}
CHOIX_TYPES = {"papier", "numerique"}
