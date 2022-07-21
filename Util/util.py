# Autheur: Charles de JAHAM
# Date : 23/04/2022
# inputFunc.py
# Ce fichier regroupe les functions d'input utilisateur
# Les fonctions limite l'entrée utilisateur à un seul type

def inputInt(printMessage: str):
    print(printMessage)
    while True:
        try:
            number = int(input(">"))
        except Exception as e:
            print(e)
        else:
            return number


def inputPositiveInt():
    while True:
        try:
            number = int(input(">"))
            if (number < 0):
                raise Exception('Entrez un nombre positif !')
        except Exception as e:
            print(e)
        else:
            return number


def inputFloat(printMessage: str):
    print(printMessage)
    while True:
        try:
            number = float(input(">"))
        except Exception as e:
            print(e)
        else:
            return number


# Retourne le caractere entier entré par l'utilisateur
def inputChar():
    while True:
        try:
            char = input(">")
            if (len(char) > 2):
                raise Exception('Entrez un seul caractere !\n')
        except Exception as e:
            print(e)
        else:
            return char
