from typing import Callable

import Exercices
from Exercices.Exercice1 import exercice1
from Exercices.Exercice2 import exercice2
from Exercices.Exercice3 import exercice3
from Exercices.Exercice4 import exercice4


def menu() -> int:
    return exercice1() + exercice2() + exercice3() + exercice4()


if __name__ == '__main__':
    menu()


