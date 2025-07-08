def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def afficher_premiers_jusqua(limite):
    compteur = 0
    print(f"\nNombres premiers de 0 à {limite} :")
    for i in range(limite + 1):
        if est_premier(i):
            print(i, end=" ")
            compteur += 1
    print(f"\n\nTotal de nombres premiers trouvés : {compteur}")

def trouver_1000e_nombre_premier():
    compteur = 0
    nombre = 2
    while compteur < 1000:
        if est_premier(nombre):
            compteur += 1
        nombre += 1
    return nombre - 1

print("NOMBRES PREMIERS - TP MODULE 3")
print("1. Afficher les nombres premiers entre 0 et 1000")
print("2. Afficher les nombres premiers jusqu'à une limite personnalisée")
print("3. Trouver le 1000e nombre premier")
choix = input("Choisissez une option (1, 2 ou 3) : ")

if choix == "1":
    afficher_premiers_jusqua(1000)

elif choix == "2":
    try:
        limite = int(input("Entrez la limite supérieure (≥ 2) : "))
        if limite < 2:
            print("La limite doit être supérieure ou égale à 2.")
        else:
            afficher_premiers_jusqua(limite)
    except ValueError:
        print("Entrée invalide. Veuillez entrer un entier.")

elif choix == "3":
    resultat = trouver_1000e_nombre_premier()
    print(f"\nLe 1000e nombre premier est : {resultat}")

else:
    print("Choix non valide. Veuillez entrer 1, 2 ou 3.")
