def terme_suivant(terme):
    resultat = []
    compteur = 1
    for i in range(1, len(terme)):
        if terme[i] == terme[i - 1]:
            compteur += 1
        else:
            resultat.append(str(compteur))
            resultat.append(terme[i - 1])
            compteur = 1
    resultat.append(str(compteur))
    resultat.append(terme[-1])
    return ''.join(resultat)

def generer_suite(profondeur):
    suite = ["1"]
    for _ in range(profondeur - 1):
        suivant = terme_suivant(suite[-1])
        suite.append(suivant)
    return suite

def afficher_suite(suite):
    for i, terme in enumerate(suite, 1):
        print(f"{i}: {terme}")

def main():
    try:
        profondeur = int(input("Profondeur de la suite: "))
        if profondeur < 1:
            print("Valeur invalide.")
            return
        suite = generer_suite(profondeur)
        afficher_suite(suite)
    except ValueError:
        print("Entrée invalide.")

main()
