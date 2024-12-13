class Carte:
    VALEURS_VALIDES = {
        '2': '2', '3': '3', '4': '4', '5': '5',
        '6': '6', '7': '7', '8': '8', '9': '9',
        '10': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'
    }
    SYMBOLES = {
        '\u2665': 'h',
        '\u2666': 'd',
        '\u2663': 'c',
        '\u2660': 's'
    }

    def __init__(self, valeur, couleur):
        if valeur not in self.VALEURS_VALIDES:
            raise ValueError(f"Valeur de carte invalide : {valeur}")
        if couleur not in self.SYMBOLES:
            raise ValueError(f"Couleur de carte invalide : {couleur}")

        self.valeur = valeur
        self.couleur = couleur

    def to_treys_format(self):
        """Convertit la carte au format attendu par treys."""
        valeur = self.VALEURS_VALIDES[self.valeur]
        symbole = self.SYMBOLES[self.couleur]
        return f"{valeur}{symbole}"

    def __str__(self):
        """Affichage lisible d'une carte."""
        return f"{self.valeur} de {self.couleur}"
