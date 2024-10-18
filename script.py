"""
Ce programme est constitué de quatre fichiers : script.py qui est le fichier principal, Fonctions.py,
Constantes.py et Mes_classes.py. Il est n'est donc pas utile de rappeler que, pour que ce programme
fonctionne, tous ces quatre fichiers doivent impérativement être mis dans le même dossier - pourquoi pas les
laisser dans le repertoire d'origine, Bibliothèque.

Lorsqu'on joue avec ce programme, douze tâches sont possibles et visibles dès le lancement du script contenu dans
le fichier principal. Ainsi, pour profiter pleinement du potentiel offert par ce programme, il est conseillé
de commencer par ajouter des utilisateurs : il s'agit des Administrateurs (admin) et des Usagers (usager) de la
Bibliothèque Docstring, qui est le nom donné à ce programme. Lors de la création d'un utilisateur, un nom et 
un prénom - pour distinguer des utilisateurs ayant le même nom de famille - et un statut (admin ou usager)
doivent lui être attribués. Le statut, c'est ce qui lui confère des autorisations pour réaliser ou non
certaines tâches, ainsi un utilisateur avec le statut d'admin peut ajouter des livres, tandis que celui avec 
le statut d'usager n'est pas autorisé à effectuer cette tâche.

Une fois que les utilisateurs sont créés, il faudra ensuite fournir au programme de la matière dont il a
besoin pour remplir pleinement rôle. Il est question ici d'ajouter des livres avec pour paramètres :
l'ISBN, titre, auteur et la classe (livre papier ou numérique) auquelle appartient le livre. Dans le programme 
le mot qui représente l'appartenance à la classe est "type_id".
Avant d'exécuter une tâche nécessitant une autorisation, comme par exemple supprimer un utilisateur,le programme 
va demander, par un message, de lui fournir le nom et prénom pour valider l'exécution de la tâche. Dans ce cas,
il faudra lui fournir le nom et le prénom d'un Administrateur. Pour le reste, en lui-même, l'exécution du programme
reste assez lisible d'autant que celle-ci demande par message tout ce qu'elle a besoin.

Enfin, ce programme offre la possibilité de sauvegarder des données dans plusieurs fichiers json. Pour ce faire, 
il suffit simplement de choisir l'option 10 (sauvegarder les données) ; cinq fichiers seront ainsi automatiquement
créés:
01.json, contiendra un dictionnaire (clé = nom et prénom, valeur = type_id) contenant tous les utilisateurs qui ont 
été fournis au programme.

02.json, y figure un dictionnaire (clé = ISBN, valeur = {"titre": titre, "auteur": auteur, "type_id": type_id}) 
contenant tous les livres (papiers ou numériques) disponibles au moment de l'exécution de la ligne de la tâche,
sauvegarder les données.

03.json, quant à lui, va contenir un dictionnaire ne contenant que des livres papiers disponibles au moment de 
l'exécution.

04.json, à l'inverse du fichier 03.json, ne contiendra qu'un dictionnaire des livres numériques.

05.json, contrairement aux trois précédents fichiers, il contiendra bien un dictionnaire dans lequel la clé
sera l'ISBN du livre emprunté et la valeur, un tuple, composé du nom de l'emprunteur et de la valeur de la
clé ISBN tel qu'il figurait dans les précédents dictionnaires avant l'emprunt. Vous l'aurez compris,
ce dernier fichier json contiendra toutes les informations nécessires sur le livre emprunté et sur la personne 
ayant emprunté le livre.
"""

import sys

from Constantes import MESSAGE_ACCUEIL, CHOIX_POSSIBLES, CHOIX_TYPES, MESSAGE_01, MESSAGE_02, MESSAGE_03, MESSAGE_04, MESSAGE_05, MESSAGE_06, MESSAGE_09
from Mes_Classes import Bibliotheque, Utilisateur
from Fonctions import statut_utilisateur, validation, parametres


print(MESSAGE_ACCUEIL)

while True:
    choix = input(MESSAGE_01)

    if choix not in CHOIX_POSSIBLES:
        print(MESSAGE_02)

    if choix == "0":
        mot_passe = input(MESSAGE_09)
        print(Bibliotheque("La Bibliothèque de Docstring").charger_donnees(mot_passe))


    elif choix == "1":
        nom = input(MESSAGE_04).lower()
        statut = input("Statut : usager ou admin ? ")
        print(Bibliotheque("La Bibliothèque de Docstring").ajouter_utilisateur(nom, statut))
    

    elif choix == "2":
        titre = (input("Titre : ")).lower()
        auteur = (input("Nom et prénom de l'auteur : ")).lower()

        while True:
            isbn = input("ISBN, un nombre de treize chiffres : ")
            if isbn.isdigit() and len(isbn) == 13:
                isbn = int(isbn)
                break

        while True:
            type_id = (input("Type : papier ou numerique ? : ")).lower()
            if type_id in CHOIX_TYPES:
                break

        nom = input(MESSAGE_06).lower()
        statut = statut_utilisateur(nom)
        print(Utilisateur(nom, statut).ajouter_livre(isbn, titre, auteur, type_id))

    elif choix == "3":
        isbn = input("ISBN à supprimer : ? ")
        nom = input(MESSAGE_06).lower()
        statut = statut_utilisateur(nom)
        print(Utilisateur(nom, statut).supprimer_livre(isbn))

    elif choix == "4":
        mot = input("Mot-clé (ISBN, Titre ou Auteur) : ")
        nom = input(MESSAGE_04).lower()
        statut = statut_utilisateur(nom)
        print(Utilisateur(nom, statut).rechercher_livre(mot))

    elif choix == "5":
        while True:
            isbn = input("ISBN, un nombre à treize chiffre : ")
            nom_emprunteur = input("Nom et prénom de l'emprunteur : ").lower()
            nom = input(MESSAGE_06)       
            if nom_emprunteur in Bibliotheque.mon_dico and nom in Bibliotheque.mon_dico:
                statut = Bibliotheque.mon_dico.get(nom)
                break
            print(f"{nom_emprunteur} n'est pas connu du système.")

        print(Utilisateur(nom, statut).emprunter_livre(isbn, nom_emprunteur))
    
    elif choix == "6":
        while True:
            isbn = input("ISBN : ? ")
            nom_emprunteur = (input("Nom et prénom de l'emprunteur, exemple : Leduc Tom ? ")).lower()
            nom = input(MESSAGE_06).lower()
            statut = statut_utilisateur(nom)

            if statut == "inconu":
                print(f"{nom} n'est pas habilité à effectuer cette opération.")
            elif statut != "inconnu":
                break
            
        print(Utilisateur(nom, statut).retourner_livre(isbn, nom_emprunteur))

    elif choix == "7":
        nom, statut = validation()
        print(Utilisateur(nom, statut).lister_livre())

    elif choix == "8":
        nom, statut = parametres()
        print(Bibliotheque("La Bibliothèque de Docstring").statistiques(nom, statut))
    
    elif choix == "9":
        nom, statut = parametres()
        print(Bibliotheque("Docstring").lister_utilisateur(nom, statut))
    
    elif choix == "10":
        nom, statut = parametres()
        print(Bibliotheque("La Bibliothèque de Docstring").sauvegarder(nom, statut))
    
    elif choix == "11":
        nom = input(MESSAGE_05).lower()
        nom_op = input(MESSAGE_06).lower()
        print(Bibliotheque("La Bibliothèque de Docstring").supprimer_utilisateur(nom, nom_op))

    elif choix == "13":
        pass

    elif choix == '13':
        print(MESSAGE_03)
        sys.exit()