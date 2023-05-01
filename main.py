import hashlib, logging, random, time
from datetime import datetime


logging.basicConfig(filename="logs/"+(datetime.now().strftime('-%Y-%m-%d-%H-%M-%S'))+".log", encoding='utf-8', level=logging.DEBUG,format='%(levelname)s:%(message)s')


def md5(string: str):
    return hashlib.md5(bytes(string, 'utf-8')).hexdigest()


def sha256(string: str):
    return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()


def sha512(string: str):
    return hashlib.sha512(bytes(string, 'utf-8')).hexdigest()


def sha1(string: str):
    return hashlib.sha1(bytes(string, 'utf-8')).hexdigest()

def hasheur_random(lst : list):
    mp_hash = []
    for i in lst:
        choix = random.randint(1,4)
        if choix == 1:
            mp_hash.append(md5(i))
        elif choix == 2:
            mp_hash.append(sha1(i))
        elif choix == 3:
            mp_hash.append(sha256(i))
        else:
            mp_hash.append((sha512(i)))
    return mp_hash

class BruteForce:
    def __init__(self, target, lst_pwd: str, lst_pwd_decrypter)-> None :
        self.Target = target # mot de passe chiffre
        self.Len_Target = len(self.Target) if type(self.Target) == str else 0  #taille du mp
        self.PassWord_List = [] # liste des mots de passes possibles en clair
        self.PassWord_File = lst_pwd # nom du fichier
        self.__DecryptedTarget = None # statut du mot de passe
        self.lst_pwd_decrypter = lst_pwd_decrypter

        #Methode primaire
        self.open_files()
        logging.info("Started")
        logging.info(f"Fichier {self.PassWord_File} ouvert ")



    def open_files(self):
        """Ouvre et copie dans la variable Password_List les mots de passes en clairs"""
        try:
            with open(self.PassWord_File, 'r') as files:
                for i in files:
                    self.PassWord_List.append(i[:-1])
        except:
            print("Erreur, chemin de fichier incorrect ! ")

    def Force_Md5(self):
        """Chiffre et compare un mot de passe clair en MD5, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if md5(index) == self.Target:
                self.__DecryptedTarget = (index, 'MD5', md5(index))

        return False

    def Force_Sha1(self):
        """Chiffre et compare un mot de passe clair en SHA1, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if sha1(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-1', sha1(index))

        return False

    def Force_Sha256(self):
        """Chiffre et compare un mot de passe clair en SHA256, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if sha256(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-256', sha256(index))

        return False

    def Force_Sha512(self):
        """Chiffre et compare un mot de passe clair en SHA512, maj la variable __DecryptedTarget ou renvoie False"""
        for index in self.PassWord_List:
            if sha512(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-512', sha512(index))

        return False

    def dechiffrement(self):
        logging.info(f"Dechiffrement en cours hash : {self.Target}")
        self.Force_Md5()
        self.Force_Sha1()
        self.Force_Sha256()
        self.Force_Sha512()

    def dechiffrement_liste(self):
        cpt = 0
        time_1 = time.time()
        try :
            for val in self.lst_pwd_decrypter:
                self.Target = val
                self.dechiffrement()
                self.afficher()
                cpt += 1

        except TypeError:
            logging.warning("dechiffrement_liste erreur, utilisez dechiffrement()")
            print("dechiffrement_liste erreur, utilisez dechiffrement()")
        chrono = time.time() - time_1
        logging.info(f"END : {cpt} mot de passes cherché en {chrono} secondes ")
        print(f"END : {cpt} mot de passes cherché en {chrono} secondes")

    def loading(self,infos, algo):
        if infos == 1:
            print(f"{algo} -> FAIL")

    def afficher(self):
        if self.__DecryptedTarget is None:
            print(f"Le mot de passe {self.Target} n'est sois pas dans la liste ou l'algorithme de chiffrement n'est pas supporté ! ")
            logging.info("brute_force : FAIL ")
        else:
            print(f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}")
            logging.info(f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}")


# c4e51fa4c9965c2fd10d0e673f92f389ac687f5e987636bd04b819dbe883dcb4
# 3bda1abe87fde48b4e2e5aea078fb4bd
# 17b1afb6aa2090ab45f60f213766f2b4a3cb7e42a7c0b358de67acb04e3152dfc4790eb3185e7c0d821bcf73d771da150d8753d1201bde196577aac1dee29d95
# 6af526e3499685bc8b78b834092d0672676c07ab

Test = BruteForce(
    "6af526e3499685bc8b78b834092d0672676c07ab",
    'password.lst', None)
Liste_pwd = []

with open('password.lst', 'r') as files:
    for i in files:
        Liste_pwd.append(i[:-1])
Liste_pwd = hasheur_random(Liste_pwd)

Test_liste = BruteForce(None, 'password.lst',Liste_pwd)
Test_liste.dechiffrement_liste()