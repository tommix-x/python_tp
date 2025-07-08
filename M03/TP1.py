def max_value(a, b):
    return a if a > b else b

def compare(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1

def test_max_and_compare():
    try:
        x = float(input("Entrez la première valeur : "))
        y = float(input("Entrez la deuxième valeur : "))

        resultat_max = max_value(x, y)
        resultat_compare = compare(x, y)

        print(f"Valeur maximale : {resultat_max}")
        print(f"Résultat de la comparaison : {resultat_compare}")
    except ValueError:
        print("Entrée invalide.")

test_max_and_compare()
