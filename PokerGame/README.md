# Poker Game - Texas Hold'em

## Description

Ce projet implémente une simulation d'un jeu de **Poker Texas Hold'em** en utilisant **Python**. Il s'agit d'un projet de jeu de cartes dans lequel les joueurs misent des jetons en fonction de leurs mains et des cartes communes sur la table.

Le but de ce projet est de démontrer l'utilisation de la **programmation orientée objet** en Python, en simulant des joueurs, une table de poker, des cartes et en évaluant les mains pour déterminer un gagnant.

## Fonctionnalités

- Distribution de cartes aux joueurs (2 cartes cachées pour chaque joueur).
- 5 cartes communes sont distribuées en trois étapes :
  - Le **Flop** : 3 cartes.
  - La **Turn** : 1 carte.
  - La **River** : 1 carte.
- Les joueurs peuvent choisir de miser ou de se coucher à chaque étape de la partie.
- Si un joueur n'a plus de jetons, il est éliminé.
- Le gagnant est déterminé à la fin de la partie, soit par la meilleure combinaison de cartes, soit par le fait qu'il ne reste plus qu'un seul joueur.

## Structure du projet

Le projet est structuré en plusieurs fichiers Python qui modélisent les objets nécessaires au jeu :

1. **Carte.py** : Modélisation d'une carte de poker.
2. **Joueur.py** : Classe représentant un joueur (avec son nom, ses jetons, ses cartes).
3. **Table.py** : Classe représentant la table de poker (avec les joueurs et les cartes communes).
4. **Combinaison.py** : Évaluation des meilleures mains en utilisant la bibliothèque **treys** pour déterminer le gagnant.

## Installation

1. Cloner ce dépôt  :

   ```bash
   git clone https://github.com/Skibrr/PokerGame.git