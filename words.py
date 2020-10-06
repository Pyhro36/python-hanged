# -*- coding: utf-8 -*-
 
import os
import random
 
def get_random_word(filename = "words.txt"):
    """
    Renvoie un mot aleatoire parmis ceux
    contenus dans le fichier dont le nom
    est passé en paramètres, un par ligne
    """
    
    # Ouvre le fichier
    with open(filename, "r") as file:
        words = []
        
        # Lit les lignes et extrait le
        # mot uniquement (sans les
        # caractères de fin de ligne)
        for line in file.readlines():
            word = list(line)
            word.reverse()
            
            if "\n" in word:
                word.remove("\n")
                
            word.reverse()
            words.append("".join(word))
                   
    return words[random. randrange(len(words))]
    
if __name__ == "__main__":
    
    print(get_random_word())