import unicodedata
from collections import Counter

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')
    texte = ''.join(c for c in texte if c.isalpha())
    return texte

def sont_anagrammes(texte1, texte2):
    t1 = nettoyer_texte(texte1)
    t2 = nettoyer_texte(texte2)
    return Counter(t1) == Counter(t2)

def tester_anagrammes():
    t1 = input("Entrez le premier mot : ")
    t2 = input("Entrez le second mot : ")
    if sont_anagrammes(t1, t2):
        print("Ce sont des anagrammes.")
    else:
        print("Ce ne sont pas des anagrammes.")

tester_anagrammes()
