from collections import Counter

ANIMAUX = [1, 2, 3]

def get_predateur(animal):
    return 1 if animal == 3 else animal + 1

def voisins(grille, x, y):
    return [
        grille[i][j]
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if (0 <= i < len(grille)) and (0 <= j < len(grille[0])) and not (i == x and j == y)
    ]

def maj_case_centrale(grille):
    x, y = 1, 1
    centre = grille[x][y]
    autour = voisins(grille, x, y)
    predateur = get_predateur(centre)
    nb_pred = autour.count(predateur)
    nb_autres = len(autour) - nb_pred
    if nb_pred > nb_autres:
        grille[x][y] = predateur
    elif nb_pred == nb_autres and nb_pred > 0:
        from random import randint
        if randint(0, 1) == 0:
            grille[x][y] = predateur

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(str(x) for x in ligne))
    print()

grille = [
    [1, 3, 2],
    [1, 2, 1],
    [3, 2, 1]
]

print("Avant :")
afficher_grille(grille)

maj_case_centrale(grille)

print("Après :")
afficher_grille(grille)
