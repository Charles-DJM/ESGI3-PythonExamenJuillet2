from Util.util import inputFloat


def convertir_Celsius_Farenheit(C: float) -> float:
    return 32 + 1.8 * C


def convertir_Celsius_Kelvin(C: float) -> float:
    return 273 + C


def convertir_Farenheit_Celsius(F: float) -> float:
    return (F - 32) / 1.8


def exercice1() -> int:
    F = inputFloat("Entrez une température en Farenheit")
    C = convertir_Farenheit_Celsius(F)
    K = convertir_Celsius_Kelvin(C)
    print(f'{F} °F vaut {K}°K')
    return 0
