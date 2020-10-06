 # -*- coding: utf-8 -*-

import os
import pickle

scores = None

def load(filename = "scores"):
    """
    Charge en mémoire les scores depuis le fichier de données
    """
    global scores_filename
    global scores
    
    scores_filename = filename
    
    if os.path.isfile(filename):
        with open(filename, "rb") as file:
            scores = pickle.load(file)
    else:
        scores = {}

def get_scores():
    """
    Renvoie le dictionnaires des scores par nom de joueur
    """

    if scores == None:
        raise Error("Les scores ne sont pas chargés !")
    
    return scores

def save():
    """
    Enregistre le fichier de scores
    """
    
    if scores == None:
        raise Error("Les scores ne sont pas chargés !")
        
    
    with open(scores_filename, "wb") as file:
        unpickler = pickle.dump(scores, file)
