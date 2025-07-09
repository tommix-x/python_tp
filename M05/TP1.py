import unicodedata
import string

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')
    texte = ''.join(c for c in texte if c.isalnum())
    return texte

def est_palindrome(texte):
    texte_nettoye = nettoyer_texte(texte)
    return texte_nettoye == texte_nettoye[::-1]

def tester_palindrome():
    phrase = input("Entrez un mot : ")
    if est_palindrome(phrase):
        print("C'est un palindrome.")
    else:
        print("Ce n'est pas un palindrome.")

tester_palindrome()
