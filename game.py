# -*- coding: utf-8 -*-

from constants import *

import scores_manager as scm
import words

_scores = None
_to_find = None
    
def init_scores(name):
    """
    Initialise le score du joueur a
    partir du nom passé en paramètres
    depuis celui enregistré ou à 0 sinon
    """
    global _scores
    global _name
    
    scm.load()
    _scores = scm.get_scores()
    _name = name
       
    # si pas déjà enregistré, initie à 0
    if _name not in _scores:
    	_scores[_name] = 0

def init_game():
    """
    Initie le jeu en lui même : le mot et les tours restants
    """
    global _to_find
    global _found
    global _found_str
    global _countdown
    
    # Choisir un mot dans un fichier
    _to_find = words.get_random_word()
    
    # Initie les variables de jeu
    _found_str = "*" * len(_to_find)
    _found = list(_found_str)
    _countdown = START_COUNTDOWN

def get_player_score():
    """
    Renvoie le score actuel du joueur,
    Lève une erreur si init_scores() n'a
    pas été déjà appelé
    """
    
    _verify_scores_initialized()
     
    return _scores[_name]

def get_to_find():
    """
    Renvoie le mot à trouver
    """
    
    _verify_game_initialized()
    
    return _to_find

def get_found():
    """
    Renvoie le mot déjà trouvé
    """
    
    _verify_game_initialized()
    
    return _found_str

def get_countdown():
    """
    Renvoie Vrai si le joueur peut encore
    jouer, faux sinon
    """
    
    _verify_game_initialized()
       
    return _countdown
    
def can_play():
    """
    Renvoie Vrai si le joueur peut encore
    jouer, faux sinon
    """
    
    _verify_game_initialized()
    
    return _found_str != _to_find and _countdown > 0

def find(proposal):
    """
    Renvoie Vrai si la proposition de
    lettre passée en paramètres est dans
    le mot à trouver et la remplace dans
    le mot trouver et Faux sinon.
    proposal doit un être une chaîne
    d'une seule lettre, lève une erreur 
    sinon
    """
    global _found
    global _found_str
    global _countdown
    
    if not (isinstance(proposal, str) and len(proposal) == 1):
        raise ValueError("proposal doit être une chaîne d'une seule lettre")
    
    _verify_game_initialized()
    
    index = _to_find.find(proposal)
    
    if index != -1:
        while index != -1:
             _found[index] = proposal
             index = _to_find.find(proposal, index + 1)
                
        _found_str = "".join(_found)
        return True
    
    else:
        _countdown -= 1
        return False

def result():
    """
    Donne le resultat du jeu : Vrai si gagné, Faux si perdu, et enregistre le score si gagné
    """
    global _scores
    
    _verify_game_initialized()
    _verify_scores_initialized()
    
    if _to_find == _found:
        _scores[_name] += _countdown
        scm.save()
        return True
    
    else:
        return False


def _verify_scores_initialized():
    """
    Verifie que les scores sont bien initialisés
    """
    
    if _scores == None:
        raise RuntimeError("Scores non initialisés ! Appelez d'abord init_score()")
    
def _verify_game_initialized():
    """
    Verifie que le jeu est bien initialisé
    """
    
    if _to_find == None:
        raise RuntimeError("Jeu on initialisé ! Appelez d'abord init_game()")
