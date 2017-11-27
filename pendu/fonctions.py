#!usr/bin/python
# -*- coding: utf-8 -*-

"""Fonctions utiles a l'application."""

from random import randrange
import donnees
import pickle
import os


def get_user():
    """Get user name."""
    name = raw_input('Entrez votre nom: \n')
    name = name.capitalize()
    if not name.isalpha():
        print('Nom invalide')
        return get_user()
    return name


def select_word(liste):
    """Randomly select a word in a given list of words."""
    n = len(liste)
    i = randrange(0, n)
    word = liste[i]
    return word


def get_letter():
    """Get a letter entered by user."""
    lettre = raw_input('Entrez une lettre: \n')
    lettre = lettre.lower()
    # Verifier qu'il s'agit bien d'une lettre
    if len(lettre) != 1 or not lettre.isalpha():
        print('Lettre invalide')
        return get_letter()
    return lettre


def get_scores():
    """Get scores dict."""
    # Verifier que le fichier existe
    dic_scores = {}
    if os.path.exists(donnees.fichier_scores):
            with open(donnees.fichier_scores, 'rb') as fichier:
                # Creation d'un depickler pour recup les scores
                depickler = pickle.Unpickler(fichier)
                dic_scores = depickler.load()
    return dic_scores


def save_scores(dic_scores):
    """Save new scores in a dictionnary."""
    with open(donnees.fichier_scores, 'wb') as fichier:
        pickler = pickle.Pickler(fichier)
        pickler.dump(dic_scores)


def get_missing_letters(chosen_word, found_letters):
    """
    Replace letters that were not found by * in chosen word.

    - chosen_word : str
    - found_letters : list of letters
    """
    seen_word = ''

    for letter in chosen_word:
        if letter in found_letters:
            seen_word += letter
        else:
            seen_word += '*'
    return seen_word


def continue_game():
    """Ask user if he wants to pursue the game."""
    user_input = raw_input('Nouvelle partie? (Y/n)')
    if user_input == 'Y' or user_input == 'y':
        continuer = 1
        return continuer
    elif user_input == 'N' or user_input == 'n':
        continuer = 0
        return continuer
    else:
        print('Incorrect input')
        return continue_game()
