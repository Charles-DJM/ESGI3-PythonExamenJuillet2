
def consomationKWH(nouveau: int, ancien: int) -> int:
    conso = nouveau - ancien
    return conso


def payeKWH(nbKWH: int, tva: float = 8.0) -> float:
    paye = 200.0
    consoZeroCent = consomationKWH(nbKWH, 100)
    if consoZeroCent <= 0:
        paye += + 0.100 * nbKWH
        return paye
    else:
        paye += 0.100 * 100
        nbKWH = nbKWH -100

    consocentCentCinquante = consomationKWH(nbKWH, 150)
    if consocentCentCinquante <= 0:
        paye += 0.175 * nbKWH
        return paye
    else:
        paye += 0.175 * 150
        nbKWH = nbKWH - 150

    paye += 0.225 * nbKWH
    paye += (paye * tva) / 100
    return paye


def exercice2() -> int:
    print(f'Prix 0KWH = {payeKWH(0)}\n')
    print(f'Prix 100KWH = {payeKWH(100)}\n')
    print(f'Prix 250KWH = {payeKWH(250)}\n')
    print(f'Prix 1000KWH = {payeKWH(1000)}\n')
    return 0
