from Table import Table
from Joueur import Joueur

def main():
    """
    Fonction principale pour exécuter une partie de Texas Hold'em Poker.
    """
    # Créer une table de jeu
    table = Table()

    # Demander le nombre de joueurs
    nombre_joueurs = int(input("Entrez le nombre de joueurs (2 à 10) : "))
    while nombre_joueurs < 2 or nombre_joueurs > 10:
        nombre_joueurs = int(input("Veuillez entrer un nombre de joueurs valide (entre 2 et 10) : "))

    # Ajouter les joueurs à la table
    for i in range(nombre_joueurs):
        nom_joueur = input(f"Entrez le nom du joueur {i+1}: ")
        joueur = Joueur(nom_joueur)
        table.ajouter_joueur(joueur)

    # Distribuer les cartes aux joueurs
    table.distribuer_cartes()

    # Afficher les cartes distribuées à chaque joueur
    print("\nCartes des joueurs :")
    for joueur in table.joueurs:
        cartes_joueur = [str(carte) for carte in joueur.cartes]
        print(f"{joueur.nom} a les cartes : {cartes_joueur}")

    # Déroulement des phases du jeu
    phases = ["Flop", "Turn", "River"]
    for phase in phases:
        print(f"\nPhase : {phase}")
        if phase == "Flop":
            table.flop()
        elif phase == "Turn":
            table.turn()
        elif phase == "River":
            table.river()

        print(f"Cartes communes : {[str(carte) for carte in table.cartes_communes]}")

        # Phase de mise
        print("\nPhase de mise :")
        for joueur in list(table.joueurs):
            if joueur.jetons == 0:
                print(f"{joueur.nom} n'a plus de jetons et se couche automatiquement.")
                joueur.se_coucher()
                table.joueurs.remove(joueur)
                continue

            while True:
                action = input(f"{joueur.nom}, voulez-vous miser ou vous coucher ? (miser/se coucher): ").lower()
                if action == "miser":
                    while True:
                        try:
                            montant = int(input("Entrez le montant de votre mise : "))
                            if montant > joueur.jetons:
                                print("Erreur : Montant de mise supérieur aux jetons disponibles.")
                                continue
                            joueur.miser(montant)
                            table.pot += montant  # Ajouter au pot commun
                            print(f"Il y a {table.pot} $ sur la table")
                            break
                        except ValueError:
                            print("Erreur : Veuillez entrer un montant valide.")
                    break
                elif action == "se coucher":
                    print(f"{joueur.nom} se couche.")
                    joueur.se_coucher()
                    table.joueurs.remove(joueur)
                    break
                else:
                    print("Action invalide. Essayez encore.")

        if len(table.joueurs) == 1:
            print(f"\n{table.joueurs[0].nom} est le dernier joueur encore en jeu !")
            break

    # Détermination du gagnant
    if len(table.joueurs) > 1:
        gagnant = table.determiner_gagnant()
        gagnant.jetons += table.pot
        table.pot = 0
        print(f"\nLe gagnant est {gagnant.nom} avec {gagnant.jetons} jetons !")
    else:
        print("\nIl n'y a pas de gagnant, tous les joueurs se sont couchés.")

if __name__ == "__main__":
    main()