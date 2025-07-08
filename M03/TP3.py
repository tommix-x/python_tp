def afficher_echiquier_sissa():
    grains = 1
    total = 0

    for ligne in range(1, 9):
        for colonne in range(1, 9):
            print(f"Ligne {ligne}, Colonne {colonne} : {grains} grain(s)")
            total += grains
            grains *= 2

    print(f"\nTotal de grains de riz sur l'échiquier : {total}")

afficher_echiquier_sissa()
