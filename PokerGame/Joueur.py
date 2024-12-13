class Joueur:
    def __init__(self, nom):
        # Initialisation d'un joueur avec un nom et des jetons
        self.nom = nom
        self.cartes = []
        self.jetons = 1000

    def recevoir_carte(self, carte):
        # Ajout d'une carte dans la main du joueur
        self.cartes.append(carte)

    def miser(self, montant):
        # Permet au joueur de miser un montant spécifié
        if montant <= 0:
            raise ValueError("Le montant de la mise doit être positif.")
        if montant > self.jetons:
            raise ValueError("Montant de mise supérieur aux jetons disponibles.")
        self.jetons -= montant
        print(f"Le joueur possède {self.jetons} jetons")
        return montant

    def se_coucher(self):
        # Permet au joueur de se coucher et de perdre toutes ses cartes
        self.cartes = []

    def reinitialiser(self):
        # Réinitialise la main du joueur pour une nouvelle manche
        self.cartes = []

    def __str__(self):
        # Affiche le nom du joueur et ses jetons restants
        return f"{self.nom} avec {self.jetons} jetons"
