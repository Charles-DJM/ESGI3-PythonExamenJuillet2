from datetime import date, datetime

def exercice3() -> int:
    tab = []
    while True:
        entry = input("Entrez un nom\n>")
        if len(entry) < 3 or len(entry) > 20:
            print("Le nom doit contenir entre 3 et 20 caractères\n")
        if entry == "FIN":
            break
        else:
            tab.append(entry)

    today = date.today().strftime("%d/%m/%Y")
    now = datetime.now().strftime("%Hh%Mm%Ss")

    print("Pour la suite de noms suivants:\n")
    print(listToString(tab))
    print("Les noms ont été sauvegardés dans le fichier pour le " + today + " à " + now)

    filename = date.today().strftime("%Y_%m_%Yd")
    filename += "_"
    filename += datetime.now().strftime("%Hh_%Mm-%Ss")
    filename += ".txt"
    print(f'dans le fichier {filename}')
    print(listToString(tab))
    with open(filename, 'w') as f:
        f.write(listToString(tab))


def listToString(tab: list) -> str:
    result = ""
    for item in tab:
        result += item + '\n'

    return result

