# -*- coding: utf-8 -*-

def format_print(format, *args, **kwargs):
    """
    Affiche la chaîne passée en
    paramètres en intégrant les
    paramètres suivants selon le
    formalisme de str.format
    """
    
    print(format.format(*args, **kwargs))