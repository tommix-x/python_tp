def calculer_grains(n_lignes, n_colonnes):
    grains = 1
    total = 0

    for ligne in range(1, n_lignes + 1):
        for colonne in range(1, n_colonnes + 1):
            print(f"Ligne {ligne}, Colonne {colonne} : {grains} grain(s)")
            total += grains
            grains *= 2

    print(f"\nTotal de grains de riz sur un échiquier {n_lignes}x{n_colonnes} : {total}")

def main():
    try:
        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        if lignes <= 0 or colonnes <= 0:
            print("Valeurs non valides")
        else:
            calculer_grains(lignes, colonnes)
    except ValueError:
        print("Entrée invalide")

main()
