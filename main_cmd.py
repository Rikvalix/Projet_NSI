from hasheur import *
from tkinter import filedialog
print("Ecran start")


def attaque_dictionnaire():
    print("1-Demo\n2-Attaque-liste\n3-Attaque-unique\n4-paramètre")
    choix = int(input(">>>"))
    match choix:
        case 1:
            pass
        case 2:
            pass
        case 3:
            txt_a_decoder = input(">>>").rstrip()
            dechiffrement_dico = DictionnaireAttaque(txt_a_decoder,"password.lst",None)
            dechiffrement_dico.dechiffrement()
            print('\n'+dechiffrement_dico.afficher())
        case 4:
            print("Le fichier password.lst doit se trouver dans le même répertoire que le .py")
        case _:
            print("choix incorrect")


def attaque_brute_force():
    pass


def chiffrement_donnees():
    print("Encodage:\n1-SHA1\n2-SHA256\n3-SHA512\n4-MD5")
    choix_endocage = int(input(">>>"))
    match choix_endocage:
        case 1:
            texte = input("texte >>>")
            print(md5(texte))
        case 2:
            texte = input("texte >>>")
            print(sha1(texte))
        case 3:
            texte = input("texte >>>")
            print(sha256(texte))
        case 4:
            texte = input("texte >>>")
            print(sha512(texte))
        case _:
            print("choix incorrect")

    return main()

def main():
    print("\n1-Attaque dictionnaire\n2-Attaque Brute Force\n3-Enchiffrement de données")
    choix_menu = int(input(">>>"))
    match choix_menu:
        case 1:
            attaque_dictionnaire()
        case 2:
            attaque_brute_force()
        case 3:
            chiffrement_donnees()
        case _:
            print("choix incorrect")

main()
