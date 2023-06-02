from tkinter import *
import tkinter.font as font
from hasheur import *

def exit():
    """ Ferme l'application"""
    quit()

def select():
    """ Recupere la selection de l'utilisateur dans les check box"""
    global selection
    selection = var.get()

def clear():
    """supprime les champs de la zone chiffrement"""
    txt_clair.delete(1.0,END)
    txt_encoder.delete(1.0,END)
def Encodage():
    """encode les informations entrer dans le champ et les renvoies"""
    if selection == 0:
        clear()
        txt_clair.insert(INSERT,"ERREUR ! Veuillez cocher une case ")
    else:
        texte_clair = txt_clair.get(1.0, END).rstrip()

        texte_encoder = ""
        if selection == 1:
            txt_encoder.delete(1.0, END)
            texte_encoder = md5(texte_clair)
        if selection == 2:
            txt_encoder.delete(1.0, END)
            texte_encoder = sha1(texte_clair)
        if selection == 3:
            txt_encoder.delete(1.0, END)
            texte_encoder = sha256(texte_clair)
        if selection == 4:
            txt_encoder.delete(1.0, END)
            texte_encoder = sha512(texte_clair)
        txt_encoder.insert(INSERT,texte_encoder)


def Launch_Demo_Dictionnaire():
    """Enchiffre le fichier password.lst puis le déchiffre a par partir de ce meme fichier"""
    liste_pwd = []
    with open('password2.lst', 'r') as files:
        for i in files:
            liste_pwd.append(i[:-1])
    liste_pwd = hasheur_random(liste_pwd)
    test_liste = DictionnaireAttaque(None, 'password2.lst', liste_pwd)
    for i in liste_pwd:
        test_liste.Target = i
        test_liste.dechiffrement()
        Area_Log.insert(INSERT, "\n"+test_liste.afficher())

def Demo_Dictionaire():
    """ Lance la démo de l'attaque dictionnaire"""
    if Demo_check.get() == 1:
        Area_Log.insert(INSERT, "\nMode Demo ACTIVE")
        Launch_Demo_Dictionnaire()
    else:
        Area_Log.insert(INSERT, "\nMode Demo DESACTIVE")




def clear_dechiffrement_dictionnaire():
    """ Clear le texte des deux consoles """
    Mp_hash.delete(1.0,END)
    Area_Log.delete(1.0,END)
def Dechiffrement_dictionnaire():
    """ Tente le dechiffrement du hash mis dans la zone de texte et affiche le resultat en console """
    if Mp_hash.get(1.0, END).rstrip() == "":
        Area_Log.insert(INSERT,"\nErreur, aucun mot de passe ")
    else:
        txt_a_decoder = Mp_hash.get(1.0,END).rstrip()
        dechiffrement_dico = DictionnaireAttaque(txt_a_decoder,"password.lst",None)
        dechiffrement_dico.dechiffrement()
        Area_Log.insert(INSERT,"\n"+dechiffrement_dico.afficher())

#Fenetre
x = 1080
y = 720
root = Tk()
root.geometry(str(x)+'x'+str(y))
root.title('Hasheur')
root.iconbitmap('assets/application.ico')
MainMenu = Menu(root)

#Fonts
Font_1 = font.Font(family= "Arial",size= 10)
Font_2 = font.Font(family="Helvetica",weight= "bold", size= 20)
# definitions
#MainMenu
first = Menu(MainMenu)
first.add_radiobutton(label = "Quitter", command=(exit)) # Quitter l'application
MainMenu.add_cascade(label = "Paramètres", menu=first)

#--------------------------------------------------CHIFFREMENT-------------------------------------------------------
Titre_Chiffrement = Label(text = "Chiffrement",font=Font_2)
Titre_Chiffrement.grid(row = 1, column= 1,padx=15,pady=5)

Message_Chiffrement = Label(text = "Veuillez choisir en quel encodage \n souhaitez vous chiffrer votre message", font = Font_1)
Message_Chiffrement.grid(row = 20, column= 1,padx=15,pady=5)

selection = 0


var = IntVar()
R1 = Radiobutton(root, text ="MD5   ", variable = var, value = 1, command = (select))
R1.grid(row = 25, column= 1)
R2 = Radiobutton(root, text ="SHA1  ", variable = var, value = 2, command = (select))
R2.grid(row = 26, column= 1)
R3 = Radiobutton(root, text ="SHA256", variable = var, value = 3, command = (select))
R3.grid(row = 27, column= 1)
R4 = Radiobutton(root, text ="SHA512", variable = var, value = 4, command = (select))
R4.grid(row = 28, column= 1)


txt_clair = Text(root, height=2, width=30)
txt_clair.grid(row = 29, column= 1,padx=15,pady=15)


RecupTexteZone = Button(root, text="Entrer", command=(Encodage),width=5)
RecupTexteZone.grid(row = 30, column= 1)

EffacerTexte = Button(root, text = "Effacer", command = (clear))
EffacerTexte.grid(row = 60, column=1)

txt_encoder = Text(root, height= 2, width= 30)
txt_encoder.grid(row = 75, column=1,padx=15,pady=15)

#--------------------------------------------------------DECHIFFREMENT----------------------------------------------------------------

Titre_Dechiffrement = Label(root, text = "Attaque Dictionnaire", font= Font_2)
Titre_Dechiffrement.grid(row = 1, column= 2 ,padx=15,pady=15)

Message_Dechiffrement = Label(root, text = "Veuillez verifier que votre fichier password.lst en clair \n est bien dans le dossier du fichier python.")
Message_Dechiffrement.grid(row = 20, column= 2,padx=15,pady=15)


Demo_check = IntVar()
R_demo_active = Radiobutton(root, text = "Mode Démo ACTIVE", variable= Demo_check, value = 1, command = (Demo_Dictionaire))
R_demo_active.grid(row = 25, column=2,padx=15,pady=15)
R_demo_desactive = Radiobutton(root, text = "Mode Démo DESACTIVE", variable = Demo_check, value = 0, command=(Demo_Dictionaire))

R_demo_desactive.grid(row = 26, column=2,padx=15,pady=15)
Mp_hash = Text(root, height=2, width=75)
Mp_hash.grid(row=27, column=2,padx=15,pady=15)

B_Entrer_Mp_Hash = Button(root, text = "Entrer", command=(Dechiffrement_dictionnaire))
B_Entrer_Mp_Hash.grid(row = 28, column= 2 )
EffacerTexte = Button(root, text = "Effacer", command = (clear_dechiffrement_dictionnaire))
EffacerTexte.grid(row = 29, column=2)
Area_Log = Text(root, height= 8, width= 75)
Area_Log.grid(row = 30, column= 2)


#Loop
root.config(menu=MainMenu)
mainloop()