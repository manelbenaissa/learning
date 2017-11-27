#!usr/bin/python
# -*- coding: utf-8 -*-

"""Jeu du pendu."""

import fonctions
import donnees

username = fonctions.get_user()
print(('Hello %s!') % (username))

# Recuperation du score courant
scores = fonctions.get_scores()
if username not in scores.keys():
    print "C'est votre premiere partie, bienvenue!"
    scores[username] = 0
score = scores[username]
print 'Votre score courant vaut %s.' % (score)


continuer = 1
while continuer == 1:
    liste_lettres = []
    mot_affiche = ''
    # Choix aleatoire d'un mot dans la liste
    mot = fonctions.select_word(donnees.liste_mots)

    print 'Vous avez %s chances pour trouver le mot' % (donnees.nb_chances)
    nb_chances = donnees.nb_chances
    while nb_chances > 0 and mot_affiche != mot:
        # On demande a l'utilisateur une lettre
        lettre = fonctions.get_letter()
        while lettre in liste_lettres:
            print 'Vous avez deja essaye cette lettre!'
            lettre = fonctions.get_letter()
        liste_lettres.append(lettre)
        if lettre not in mot:
            print 'oops'
            nb_chances = nb_chances - 1
        mot_affiche = fonctions.get_missing_letters(mot, liste_lettres)
        print mot_affiche
        print 'Il vous reste maintenant %s chance(s)' % (nb_chances)

    if mot_affiche == mot:
        print 'Felicitations!'
        score += nb_chances

    else:
        print 'Vous avez éte pendu! Plus de chances dispo!'
        print 'Le mot etait : %s' % (mot)

    print 'Votre score vaut maintenant %s' % (score)
    continuer = fonctions.continue_game()

print 'Hasta luego!'
scores[username] = score
fonctions.save_scores(scores)
print 'Votre score final de %s est enregistre!' % (score)
