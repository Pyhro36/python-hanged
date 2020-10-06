# -*- coding: utf-8 -*-

from utils import *

import game

def main():
    """
    Methode principale du programme,
    porte l'initialisation, la boucle de
    jeu et le calcul du résultat.
    """
    
    # Demander le nom du joueur
    print("Bonjour ! Prêt pour une nouvelle partie de pendu ?")
    name = input("Entrez votre nom :")
    
    game.init_scores(name)
    
    format_print("Votre score actuel est de : {}", game.get_player_score());
    
    game.init_game()
    
    print("Mot choisi !\nC'est parti !")
    # Tant que pas trouver afficher le
    # mot decomposé
    first = True    
    while game.can_play():
        
        if first:
            first = False
        else:
            print("Rejouez !")
        
        format_print("Il vous reste {} coups", game.get_countdown())
        format_print("Mot à trouver : {}",game.get_found())
        
        # On cherhche la proposition du
        # joueur dans le mot à trouver
        proposal = input("Proposez une lettre :")
        
        # Proposition trouvée : on
        # l'affiche et on peut rejouer
        if game.find(proposal):
            format_print("Oui ! Il y a bien un {} dans le mot.", proposal)

        # Sinon on perd un tour
        else:
            format_print("Et non, pas de {} dans le mot !", proposal)

    # Si trouvé en moins de 8 coups
    # enregistre le score
    if game.result():
        format_print("Gagné !\nLe mot était bien {word}\nVous gagnez {score} points de score", word=game.get_to_find(), score=game.get_countdown())

    # Sinon, perdu !
    else:
        format_print("Perdu !\nLe mot était : {}", game.get_to_find())
        
if __name__ == "__main__":
    
    main()