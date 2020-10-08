 # -*- coding: utf-8 -*-

import os
import pickle

_scores = None

def init(name, filename = "scores"):
    """
    Charge en mémoire les scores depuis
    le fichier de données, puis le score
    du joueur en particulier depuis celui
    enregistré ou à 0 sinon
    """
    global _filename
    global _scores
    global _name
    
    _filename = filename
    _name = name
    
    # Récupère ou initie le tableau des
    # scores
    if os.path.isfile(filename):
        with open(filename, "rb") as file:
            _scores = pickle.load(file)
    else:
        _scores = {}
     
    # si joueur pas déjà enregistré,
    # initie son score à 0
    if _name not in _scores:
    	_scores[_name] = 0

def get():
    """
    Renvoie le score actuel du joueur,
    Lève une erreur si init_scores() n'a
    pas été déjà appelé
    """
    
    _verify_initialized()
     
    return _scores[_name]
    
def add(gain):
    """
    Ajoute le gain de la partie au score
    du joueur
    """
    
    _verify_initialized()
    
    _scores[_name] += gain   

def save():
    """
    Enregistre le fichier de scores
    """
    
    _verify_initialized()     
    
    with open(_filename, "wb") as file:
        unpickler = pickle.dump(_scores, file)
        

def _verify_initialized():
    """
    Verifie que les scores sont bien initialisés
    """
    
    if _scores == None:
        raise RuntimeError("Scores non initialisés ! Appelez d'abord init_score()")
