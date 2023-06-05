import os, json


class Brute_Force:
    """Brute_Force class with all functions 
    """
    def __init__(self, hash : str) -> None:
        self.proposition = True
        self.hash = hash
    
    def open_files(self,path : str, mode = "r"):
        """Open files of password and return list with all values of the files, you have to indicate the path, mode is defaut reading
            encoding value is UTF-8 you cant change it.
            example : open_files("password.lst","w") - open_files("assets/password.lst")


        Args:
            path (str): path of the files
            mode (str, optional): Defaults to "r".

        Output:
            List : All values of the files

        Raises :
            FileNotFoundError : The path is maybe incorrect 
        """
        lst_mp = []
        if not os.path.exists(path):
            raise FileNotFoundError("Path incorrect or the file doesnt exist.")     
        else:
            with open(path,mode,encoding='UTF-8') as file:
                for i in file:
                    lst_mp.append(i[:-1])
        return lst_mp

    def bruteforce_recursif(self,word : str, length : int, length_fixe: int ,character,file : list):
        """Recursive function will add after all password, all posibilities of character.

        Args:
            word (str): the password
            length (int): dynamic values, increase after round
            length_fixe (int): numbers of characters after the word
            character (_type_): the list of characters
            file (list): variable of the file to write in the text file
        """
        if length <= length_fixe:
            for letter in character:
                file.write(word+letter+"\n")
                self.bruteforce_recursif(word + letter, length + 1, length_fixe,character,file)

    def bruteforce_completation(self, file_list: list ,length : int, path = "", name = "password_possibilities.txt" , character = ['1','2','3','4','5','6','7','8','9','0']):
        """Adding characters behind an existing known password

        Args:
            file_list(list): List of password, you can use open_files() to open your password file
            length (int): numbers of characters adding after the know password
            name (str) : name of your files, defaut values is password_possibilities.txt
            path (str) : path where you want create the files, if folder doesnt exist function will create the folder, defaut value is the folder of your code
            character(list) : list of characters which you want test, defaut is ['1','2','3','4','5','6','7','8','9','0']

        Output :
            List .txt with all possibilities 
        
        Raises :
            Files is nonexistent 
        """
        

        if not path == "":
            os.makedirs(path, exist_ok=True) 
            try: 
                file =  open(path+"/"+name,"w",encoding='UTF-8')
            except:
                raise FileNotFoundError("FileNotFound")
        else:
            try:
                file = open(name, "w",encoding='UTF-8')
            except:
                raise FileNotFoundError("FileNotFound")
        for password_word in file_list:
            self.bruteforce_recursif(self,password_word,0,length,character,file)


    def detection(self):
        try :
            with open("function_hash.json","r") as File_Object:
                File_Object = json.loads(File_Object.read())
        except :
            raise FileNotFoundError("ERROR, File function_hash.json Not found")
        








