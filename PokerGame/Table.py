from Paquet import Paquet
from treys import Evaluator, Card


class Table:
    def __init__(self):
        # Initialisation de la table avec un paquet de cartes et des joueurs
        self.cartes_communes = []
        self.joueurs = []
        self.paquet = Paquet()
        self.pot = 0

    def ajouter_joueur(self, joueur):
        # Ajoute un joueur à la table
        self.joueurs.append(joueur)

    def distribuer_cartes(self):
        # Distribue 2 cartes à chaque joueur
        for joueur in self.joueurs:
            for _ in range(2):
                if self.paquet.cartes:
                    carte = self.paquet.tirer_carte()
                    joueur.recevoir_carte(carte)
                else:
                    raise ValueError("Le paquet est vide. Impossible de distribuer les cartes.")

    def flop(self):
        # Révèle les 3 premières cartes communes (le flop)
        for _ in range(3):
            carte = self.paquet.tirer_carte()
            self.cartes_communes.append(carte)

    def turn(self):
        # Révèle la 4e carte commune (la turn)
        carte = self.paquet.tirer_carte()
        self.cartes_communes.append(carte)

    def river(self):
        # Révèle la 5e carte commune (la river)
        carte = self.paquet.tirer_carte()
        self.cartes_communes.append(carte)
    
    def determiner_gagnant(self):
        evaluator = Evaluator()
        meilleure_main = None
        gagnant = None

        for joueur in self.joueurs:
            # Convertir les cartes en format treys
            print(f"Cartes de {joueur.nom} avant conversion : {[str(carte) for carte in joueur.cartes]}")
            main = [Card.new(carte.to_treys_format()) for carte in joueur.cartes]
            cartes_communes = [Card.new(carte.to_treys_format()) for carte in self.cartes_communes]
            
            # Évaluer la main
            score = evaluator.evaluate(main, cartes_communes)
            
            if meilleure_main is None or score < meilleure_main:
                meilleure_main = score
                gagnant = joueur
            

        return gagnant
