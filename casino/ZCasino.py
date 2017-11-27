#!/usr/bin/python
# -*- coding: utf-8 -*-

"""TP OpenClassroom sur le casino."""

from __future__ import division
from random import randrange
from math import ceil
from time import sleep

print('Votre capital de départ vaut 1000$')
argent = 1000

# Le jeu continue tant qu'on a de l'argent
continuer = 1
while argent > 0 and continuer == 1:
    case = -1
    # Numéro sur lequel miser
    while case < 0 or case > 49:
        case = raw_input('Inserez un numéro entre 0 et 49: \n')
        try:
            case = int(case)
        except ValueError or NameError:
            print('Mise incorrecte')
            case = -1
            continue

    # Mise de l'utilisateur
    mise = -1
    while mise <= 0 or mise > argent:
        mise = raw_input('Insérez votre mise: \n')
        try:
            mise = int(mise)
        except ValueError:
            print("La mise insérée n'est pas un nombre")
            continue
        if mise <= 0:
            print('Il faut au moins miser 1$')
        if mise > argent:
            print('Vous ne pouvez pas miser plus que votre argent!')

    argent = argent - mise
    print('Et le numéro gagnant est...')
    numero_gagnant = randrange(50)
    sleep(2)
    print('%s !' % (numero_gagnant))
    parite_case = case % 2
    parite_num = numero_gagnant % 2

    # Cas Gagnant
    if numero_gagnant == case:
        print('Vous avez gagné')
        argent = argent + 3*mise
    # Les cases sont de la même couleur
    elif parite_num == parite_case:
        print('Vous avez misé sur la bonne couleur')
        argent = argent + ceil(mise/2)
    else:
        print('Loser!')
    print('Vous avez maintenant %s $!' % (argent))

    if argent <= 0:
        print('Fin du game, vous êtes ruiné!')
    else:
        continuer = 3
        while continuer == 3:
            user_continue = raw_input('Voulez vous continuer? (Y/n)\n')
            if user_continue == 'Y':
                continuer = 1
                print
            elif user_continue == 'n':
                continuer = 0
                print
            else:
                print('Il faut insérer Y pour oui, n pour non')
print('Le jeu est fini! Vous repartez avec vos %s $' % (argent))
