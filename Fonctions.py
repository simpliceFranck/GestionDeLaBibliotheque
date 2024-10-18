from Constantes import MESSAGE_01, MESSAGE_02, MESSAGE_04, CHOIX_POSSIBLES
from Mes_Classes import Bibliotheque


def choix_utilisateur():
    while True:
        choix = input(MESSAGE_01)

        if choix not in CHOIX_POSSIBLES:
            print(MESSAGE_02)
        
        else: 
            return choix


def statut_utilisateur(nom):
    return Bibliotheque.mon_dico.get(nom, "inconnu")


def parametres():
    nom = input(MESSAGE_04).lower()
    statut = statut_utilisateur(nom)
    return (nom, statut)


def validation():
    while True:
            nom = input(MESSAGE_04).lower()
            statut = statut_utilisateur(nom)
            if statut == "inconnu":
                print(f"Vous n'êtes pas autorisés à effectuer cette opération.")
            elif statut != "inconnu":
                break
    
    return nom, statut