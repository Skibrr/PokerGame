from Carte import Carte
import random

class Paquet:
    def __init__(self):
        # Création du paquet de 52 cartes
        self.cartes = [
            Carte(valeur, couleur)
            for valeur in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            for couleur in ['\u2665', '\u2666', '\u2663', '\u2660']
        ]
        self.melanger()

    def melanger(self):
        # Mélange les cartes du paquet
        random.shuffle(self.cartes)

    def tirer_carte(self):
        # Tire une carte au dessus du paquet
        return self.cartes.pop() if self.cartes else None
