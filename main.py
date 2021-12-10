"""
Magasság kalkulátor.
Kiszámítja egy tárgynak a magasságát az alábbi adatok alapján:
    tárgytól való távolság
    milyen szögben látszik a teteje
    milyen szögben látszik az alja
Az adatok megadhatók az alkalmazásban, vagy több adat esetén file formában.
A bemenetnek megfelelően az alkalmazásban, vagy külön fileban jelenik meg az eredmény.
Külön fileba írt végeredmény esetén lehet választani, hogy
    csak az eredményt írja ki: 123.23432
    a bemeneti adatokat is kiírja: __;__;__;123.23432
"""
from styling import Color
from osztaly import *

# Formázás
kiemel = Color.BOLD.value
hiba = Color.BOLD.value + Color.RED.value
vege = Color.END.value


def main_menu() -> None:
    """
    Kiírja a főmenü szövegét.
    :return:
    """
    print("\n" + kiemel + "Magasság kalkulátor" + vege)
    print("Egyszerre egy, vagy több magasságot szeretne számítani?")
    print("1 - Egy magasság számítása (alkalmazásban)")
    print("2 - Több magasság számítása (file alapján)")
    print("0 - Kilépés")


def magassag_menu() -> None:
    """
    Bekéri az adatokat a magasság kiszámításához, majd meghívja a magassag függvényt.\n
    :return: magasság, méterben
    """
    tavolsag = input("\nAdja meg a mért tárgy távolságát méterben: ")
    print("A következő adatokat tizedestört szög formátumban adja meg: ___.__°")
    alfa = input("Ilyen szögben látszik a tárgy teteje: ")
    beta = input("Ilyen szögben látszik a tárgy alja: ")
    try:
        b = Bemenet(tavolsag, alfa, beta)
        k = Kimenet(b.ki())
        print("A tárgy magassága %.2f méter." % k.mag)
    except ValueError:
        print(hiba + "Hibás bemeneti adatok." + vege)


def legyen_bemenet_is(path: str, adatok: list) -> None:
    """
    Bekéri, hogy a felhasználó csak a végeredményt szeretné a fileba iratni, vagy az eredeti adatokat is.
    :return: boolean
    """
    print("\nCsak az eredményt szeretné kiírni, vagy a bemeneti adatokat is?")
    kerdes = input("1 - Csak eredmény\n2 - Bemeneti adatok, eredménnyel kiegészítve\n")
    if kerdes == "1":
        kiir_bemenet_nelkul(path, adatok)
    elif kerdes == "2":
        kiir_bemenettel(path, adatok)
    else:
        print("Hibás opció.")


def kiir_bemenettel(path: str, adatok: list) -> None:
    """
    Kiírja a megadott fileba az eredményt, soronként elé írva a bemeneti adatokat is.\n
    :param path: filenév
    :param adatok: korábban kiszámolt eredmények, Kimenet osztályú objektum
    :return:
    """
    path = path + ".csv"
    fki = open(path, "w")  # Itt nem szükséges ellenőrzés, ha létezik felülírja, ha nem, akkor létrehozza
    for adat in adatok:
        k = Kimenet(adat.ki())
        kimenet = str(k.tav) + ";" + str(k.teteje) + ";" + str(k.alja) + ";" + str(k.mag) + "\n"
        fki.write(kimenet)
    fki.close()
    print("\nAz eredmények sikeresen kiírásra kerültek a bevitel sorrendjének megfelelően %s filenéven." % path)


def kiir_bemenet_nelkul(path: str, adatok: list) -> None:
    """
    Kiírja a megadoff fileba azd eredményt.\n
    :param path: filenév
    :param adatok: korábban kiszámolt eredmények, Kimenet osztályú objektum
    :return:
    """
    path = path + ".txt"
    fki = open(path, "w")  # Itt nem szükséges ellenőrzés, ha létezik felülírja, ha nem, akkor létrehozza
    for adat in adatok:
        k = Kimenet(adat.ki())
        fki.write(str(k.mag) + "\n")
    fki.close()
    print("\nAz eredmények sikeresen kiírásra kerültek a bevitel sorrendjének megfelelően %s filenéven." % path)


def file_menu() -> None:
    """
    Bekéri az adatfile elérését, megnyitja, feldolgozza, majd kiírja azt.\n
    :return: nincs
    """
    print(kiemel + "\nFontos: A bemeneti filenak egy mappában kell lennie a programmal!" + vege)
    print("Tartalma: távolság (méter);tárgy teteje (fok, tizedestört);tárgy alja (fok, tizedestört)")
    print("\t\tPl: 10;22.12;43.83")

    try:  # Filenév ellenőrzés
        path = input("Adja meg a filenevet: ")
        fbe = open(path, "r")
        sorok = []
        for line in fbe:
            sor = line.strip().split(";")
            ujsor = []
            for i in range(len(sor)):
                ujsor.append(float(sor[i]))
            sorok.append(ujsor)
        fbe.close()
        try:  # File tartalom ellenőrzés
            adatok = []
            for sor in sorok:
                b = Bemenet(sor[0], sor[1], sor[2])
                adatok.append(b)

            print("\nAdja meg, hogy milyen fileba szeretné menteni az adatokat.")

            # Nincs ellenőrizve, úgy is működik, ha pl ki.txt.txt lesz a végeredmény.
            print(kiemel + "A filenevet kiterjesztés nélkül adja meg!" + vege)
            path = input("Adja meg a filenevet: ")
            legyen_bemenet_is(path, adatok)
        except ValueError:
            print(hiba + "Hibás bemeneti adatok." + vege)
    except FileNotFoundError:
        print(hiba + "Hibás filenév." + vege)


menu = ""
while menu != "0":
    main_menu()
    menu = input()
    if menu == "1":
        magassag_menu()
    elif menu == "2":
        file_menu()
