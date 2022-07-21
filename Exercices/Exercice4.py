from random import randrange
from enum import Enum


class Couleur(Enum):
    PIQUE = 'Pi'
    COEUR = 'Co'
    CARREAU = 'Ca'
    TREFLE = 'Tr'


class Carte:
    def __init__(self, valeur: int, couleur: Couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f'{self.valeur} de {self.couleur.name}'


class Paquet:
    def __init__(self, listeCarte: list):
        self.cartes = listeCarte

    def __str__(self):
        string = ""
        for carte in self.cartes:
            string += carte.__str__() + '\n'
        return string

    def melanger(self):
        for i in range(len(self.cartes) - 1):
            number = randrange(0, len(self.cartes) - i)
            tmp = self.cartes.pop()
            self.cartes.append(self.cartes[number])
            self.cartes[number] = tmp

    @staticmethod
    def creerlistecarte():
        liste = []
        for couleur in Couleur:
            for i in range(1, 13):
                liste.append(Carte(i, couleur))

        return liste


def exercice4() -> int:
    paquet = Paquet(Paquet.creerlistecarte())
    print(paquet)
    paquet.melanger()
    print(paquet)
    return 0
