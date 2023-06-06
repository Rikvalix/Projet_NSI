import hashlib,logging, random, time, os
from datetime import datetime

os.makedirs("logs", exist_ok=True)  # verifie si le dossier logs existe sinon le creer


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/" + (datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')) + ".log","w",'utf-8')
root_logger.addHandler(handler)

def md5(string: str):
    """encryption of the data string in MD5

    Args:
        string (str): character string that will be encrypted

    Returns:
        string : returns the encrypted string
    """
    return hashlib.md5(bytes(string, 'utf-8')).hexdigest()


def sha256(string: str):
    """encryption of the data string in SHA256

    Args:
        string (str): character string that will be encrypted

    Returns:
        string : returns the encrypted string
    """
    return hashlib.sha256(bytes(string, 'utf-8')).hexdigest()


def sha512(string: str):
    """encryption of the data string in SHA512

    Args:
        string (str): character string that will be encrypted

    Returns:
        string : returns the encrypted string
    """
    return hashlib.sha512(bytes(string, 'utf-8')).hexdigest()


def sha1(string: str):
    """encryption of the data string in SHA1

    Args:
        string (str): character string that will be encrypted

    Returns:
        string : returns the encrypted string
    """
    return hashlib.sha1(bytes(string, 'utf-8')).hexdigest()


def hasheur_random(lst: list):
    """Hash le fichier de mot de passe en clair afin de faire la démo"""
    mp_hash = []
    for i in lst:
        choix = random.randint(1, 4)
        if choix == 1:
            mp_hash.append(md5(i))
        elif choix == 2:
            mp_hash.append(sha1(i))
        elif choix == 3:
            mp_hash.append(sha256(i))
        else:
            mp_hash.append((sha512(i)))
    return mp_hash


class DictionnaireAttaque:
    """Ensemble de fonctions des attaques de dictionnaire
    """

    def __init__(self, target: str, lst_pwd: str, lst_pwd_decrypter) -> None:
        """Constructeur des variables de la classe DictionnaireAttaque

        Args:
            target (str): Mot de passe chiffre
            lst_pwd (str): Liste des mots de passe en clair
            lst_pwd_decrypter (list): Liste des mots de passe chiffrer 
        """
        self.Target = target  # mot de passe chiffre
        self.Len_Target = len(self.Target) if type(self.Target) == str else 0  # taille du mp
        self.PassWord_List = []  # liste des mots de passes possibles en clair
        self.PassWord_File = lst_pwd  # nom du fichier
        self.__DecryptedTarget = None  # statut du mot de passe
        self.lst_pwd_decrypter = lst_pwd_decrypter

        # Methode primaire
        self.open_files()
        logging.info("Started")
        logging.info(f"Fichier {self.PassWord_File} ouvert ")

    def open_files(self,):
        """Open files Open files of password and return list with all values of the files, ( undevelopped ) you have to indicate the path, mode is defaut reading
            encoding value is UTF-8 you cant change it.

            Raises :
                FileNotFoundError : The path is maybe incorrect 
        """
        try:
            with open(self.PassWord_File, 'r') as files:
                for i in files:
                    self.PassWord_List.append(i[:-1])
        except:
            raise FileNotFoundError("Error, Path is maybe incorrect")

    def Dictionnaire_Md5(self):
        """Encrypts and compares a plain MD5 password, shift the __DecryptedTarget variable or return False

        Returns:
            boolean: return status of the function False = end 
        """
        for index in self.PassWord_List:
            if md5(index) == self.Target:
                self.__DecryptedTarget = (index, 'MD5', md5(index))

        return False

    def Dictionnaire_Sha1(self):
        """
        Encrypts and compares a plain SHA1 password, shift the __DecryptedTarget variable or return False

        Returns:
            boolean: return status of the function False = end 
        
        """       
        for index in self.PassWord_List:
            if sha1(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-1', sha1(index))

        return False

    def Dictionnaire_Sha256(self):
        """Encrypts and compares a plain SHA256 password, shift the __DecryptedTarget variable or return False

        Returns:
            boolean: return status of the function False = end """
        for index in self.PassWord_List:
            if sha256(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-256', sha256(index))

        return False

    def Dictionnaire_Sha512(self):
        """Encrypts and compares a plain SHA512 password, shift the __DecryptedTarget variable or return False

        Returns:
            boolean: return status of the function False = end """
        for index in self.PassWord_List:
            if sha512(index) == self.Target:
                self.__DecryptedTarget = (index, 'SHA-512', sha512(index))

        return False

    def dechiffrement(self):
        """Try every string decryption function
        """
        logging.info(f"Dechiffrement en cours hash : {self.Target}")
        self.Dictionnaire_Md5()
        self.Dictionnaire_Sha1()
        self.Dictionnaire_Sha256()
        self.Dictionnaire_Sha512()

    def dechiffrement_liste(self):
        """Try list string decryption function
        """
        cpt = 0
        time_1 = time.time()
        try:
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

    def afficher(self):
        """Show results

        Returns:
            string (str): result
        """
        if self.__DecryptedTarget is None:
            logging.info("brute_force : FAIL ")
            return f"Le mot de passe {self.Target}n'est soit pas dans la liste ou l'algorithme de chiffrement n'est pas supporté ! "
        else:
            logging.info(
                f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}")
            return f"Déchiffré : {self.__DecryptedTarget[0]}, encodage : {self.__DecryptedTarget[1]}, hash : {self.__DecryptedTarget[2]}"


class AttaqueBruteForce:
    def __init__(self, password):
        self.caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                           'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
                           '5', '6', '7', '8', '9', ',', '?', ';', '.', ':', '/', '!', '§', 'ù', '%', '*',
                           'µ', '$', '£', '^', '¨', '&', 'é', '~', '#', "'", '(', '[', '-', '|', 'è', '`', '_', '\\',
                           'ç', '^', 'à', '@', ')', ']', '°', '+', '=', '}', '"']
        self.password = password
        self.caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def Brute_Force(self, word, longueur):
        if longueur <= 5:
            for letter in self.caracteres:
                if self.password == word + letter:
                    print(f"Mdp : {word + letter}")
                else:
                    # print(word + letter)
                    self.Brute_Force(word + letter, longueur + 1)
