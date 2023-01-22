import csv

with open('Zeszyt.csv', 'r') as f:
    odczyt = csv.reader(f, delimiter=';')
    lista = list(odczyt)
with open('2020.csv','r')as g:
    wczytaj=csv.reader(g,delimiter=';')
    listaUbieglo=list(wczytaj)

def wyswietlPowiatyz2020():
    for kolumna in listaUbieglo:
        print(kolumna)
        przerwa()

def wyswietlWszystkiePowiiaty():
    for kolimna in lista:
        print(kolimna)
        przerwa()

def obliczŚredniąWPolsce():
    sumaProcenty = 0
    sumaIloscWTys = 0
    iloscPowiatow = 0
    for kolumna in lista:
        sumaProcenty += float(kolumna[2].replace(',', '.'))
        sumaIloscWTys += float(kolumna[1].replace(',', '.'))
        iloscPowiatow = iloscPowiatow + 1
    sredniaProcent = sumaProcenty / iloscPowiatow
    sredniaWTys = sumaIloscWTys / iloscPowiatow
    przerwa()

    return (sredniaProcent, sredniaWTys)


def ileBezrobotnychWPolsce():
    ileBezrobotnychWTys = 0
    for kolumna in lista:
        ileBezrobotnychWTys += float(kolumna[1].replace(',', '.'))

    return ileBezrobotnychWTys


def ilemieszkańcówWPolsce():
    ileMieszkańcówWTys = 0
    for kolumna in lista:
        ileBezrobotnychWPowiecie = float(kolumna[1].replace(',', '.'))
        procentBezrobotnych = float(kolumna[2].replace(',', '.'))
        liczbaMieszkanowPowiatu = ileBezrobotnychWPowiecie * 100.0 / procentBezrobotnych

        ileMieszkańcówWTys += liczbaMieszkanowPowiatu
    return ileMieszkańcówWTys


def bezrobocieWPolsce():
    return ileBezrobotnychWPolsce() / ilemieszkańcówWPolsce()


def daneOWojewodztwie(wojewodztwo):
    sumaProcent = 0
    sumaIlosc = 0
    iloscPowiatowWWojewodztwie = 0
    listaa = ileMieszkancowWWojewodztwach()
    print("Ilość mieszkańców:")
    print(listaa.get(wojewodztwo.upper()))
    for kolumna in lista:
        if wojewodztwo.upper() == kolumna[3].upper():
            print("Nazwa Powiatu"+kolumna[0]+" Ilosć bezrobotnych w tys "+kolumna[1]+" co stanowi "+kolumna[2]+"%")
            sumaIlosc += float(kolumna[1].replace(',', '.'))
            sumaProcent += float(kolumna[2].replace(',', '.'))
            iloscPowiatowWWojewodztwie = iloscPowiatowWWojewodztwie + 1

    sredniaProcent = sumaProcent / iloscPowiatowWWojewodztwie
    sredniaWTys = sumaIlosc / iloscPowiatowWWojewodztwie
    przerwa()

    return sredniaProcent, sredniaWTys


def daneOPowiecie(powiat):
    for kolumna in lista:
        if powiat.upper() == kolumna[0].upper():
            print(kolumna)
            przerwa()
            return powiat


def sortujPoIlosc():
    lista.sort(key=lambda lista: lista[1].replace(',', '.'))


def sortujPoProcencie():
    lista.sort(key=lambda lista: lista[2].replace(',', '.'))


def RankingPoiatowPoIlosci():
    sortujPoIlosc()
    for kolumna in lista:
        print(kolumna[0])
        przerwa()


def RankingPowiatowPoProcencie():
    sortujPoProcencie()
    for kolumna in lista:
        print(kolumna[0])
        przerwa()


def dzialanieProgramu():
    wybor = 0
    while wybor != 7:
        przerwa()
        print('1.Informacje o Polsce')
        print('2.Dane o Województwie')
        print('3.Dane o Powiecie')
        print('4.Ranking Województw')
        print('5.Ranking powiatow')
        print('6.Porównanie obecnego bezrobocia względem 2020')
        print('7.Wyjscie')
        wybor = int(input('Wybierz dzialanie '))

        if (wybor == 1):
            srednieBezrobocieNaPowiatWProcentach, srednieBezrobocieNaPowiatWTys = obliczŚredniąWPolsce()
            print("Srednia ilosc bezrobotnych na 1 powiat: ",
                  "{:.3f}".format(srednieBezrobocieNaPowiatWProcentach) + " tys.")
            print("Sredni procent bezrobocia na 1 powiat: ", "{:.2f}".format(srednieBezrobocieNaPowiatWTys) + "%. ")
            print("Ile badanych w Polsce : ", "{:.3f}".format(ilemieszkańcówWPolsce()) + " tys.")
            print("Ile bezrobotnych w Polsce: ", "{:.3f}".format(ileBezrobotnychWPolsce()) + " tys.")
            print("Procent bezrobotnych w Polsce", "{:.2f}".format(bezrobocieWPolsce() * 100) + "%.")
        if (wybor == 2):
            wojewodztwo = input("Podaj nazwę województwa")
            daneOWojewodztwie(wojewodztwo)
        if (wybor == 3):
            powiat = input("Podaj nazwę powiatu")
            daneOPowiecie(powiat)
        if (wybor == 4):
            wojewodztwaRanking()
        if (wybor == 5):
            RankingPowiatowPoProcencie()
            RankingPoiatowPoIlosci()
        if(wybor ==6):
            powiat = input("Podaj nazwę powiatu")
            porownajDaneztegoiPoprezedniego(powiat)
        if (wybor == 7):
            print("Koniec")


def ileBezrobotnychWWojewodztwach():
    ileBezrobotnych = {}
    for kolumna in lista:
        nazwaWojewodztwa = kolumna[3]
        ileBezrobotnychWPowiecie = float(kolumna[1].replace(',', '.'))

        if nazwaWojewodztwa in ileBezrobotnych:
            ileBezrobotnych[nazwaWojewodztwa] += ileBezrobotnychWPowiecie
        else:
            ileBezrobotnych[nazwaWojewodztwa] = ileBezrobotnychWPowiecie

    return ileBezrobotnych

def porownajDaneztegoiPoprezedniego(powiat):
    wynik1=0
    wynik2=0
    for kolumna in lista:
        if powiat.upper() == kolumna[0].upper():
            wynik1=float(kolumna[1].replace(',', '.'))
            wynik1pr=float(kolumna[2].replace(',', '.'))

    for kolumna in listaUbieglo:
        if powiat.upper() == kolumna[0].upper():
            wynik2=float(kolumna[1].replace(',', '.'))
            wynik2pr=float(kolumna[2].replace(',', '.'))
    if wynik1>wynik2:
        roznicapr=wynik1pr-wynik2pr
        procent=wynik1*100/wynik2
        print("Bezrobocie spadło o :")
        print(roznicapr)
        print("Zmalało o:")
        print(procent-100)
    if wynik2>wynik1:
        roznicapr=wynik2pr-wynik1pr
        print("Bezrobocie wzrosło o (tys):")
        print(roznicapr*100)
        procent = wynik2 * 100 / wynik1
        print("Wzrosło o(%):")
        print(procent - 100)
        przerwa()
def wojewodztwaRanking():
    ileBezrobotnych = ileBezrobotnychWWojewodztwach()
    print("Ilosc bezrobotnych w tys. w kazdym z wojewodztw:")
    print(ileBezrobotnych)

    ileMieszkancow = ileMieszkancowWWojewodztwach()
    print("Ilosc mieszkancow w tys. w kazdym z wojewodztw:")
    print(ileMieszkancow)
    srednieBezrobocie = srednieBezrobocieWWojewodztwach(ileBezrobotnych, ileMieszkancow)
    srednieBezrobocieLista = []
    for wojewodztwo in srednieBezrobocie:
        srednieBezrobocieLista.append((wojewodztwo, srednieBezrobocie[wojewodztwo]))
    srednieBezrobocieLista.sort(key=lambda para: float(para[1][:-1]))
    print("Bezrobocie wg wojewodztw od najmniejszego: ", srednieBezrobocieLista)
    print("Najwieksze bezrobocie:", srednieBezrobocieLista[-1])
    print("Najmniejsze bezrobocie:", srednieBezrobocieLista[0])
    przerwa()


def ileMieszkancowWWojewodztwach():
    ileLudzi = {}
    for kolumna in lista:
        nazwaWojewodztwa = kolumna[3]
        ileBezrobotnychWPowiecie = float(kolumna[1].replace(',', '.'))
        procentBezrobotnych = float(kolumna[2].replace(',', '.'))

        liczbaMieszkanowPowiatu = ileBezrobotnychWPowiecie * 100.0 / procentBezrobotnych

        if nazwaWojewodztwa in ileLudzi:
            ileLudzi[nazwaWojewodztwa] += liczbaMieszkanowPowiatu
        else:
            ileLudzi[nazwaWojewodztwa] = liczbaMieszkanowPowiatu

    return ileLudzi


def srednieBezrobocieWWojewodztwach(ileBezrobotnych, ileMieszkancow):
    bezrobocieWWojewodztwie = {}

    for wojewodztwo in ileBezrobotnych:
        procent = ileBezrobotnych[wojewodztwo] / ileMieszkancow[wojewodztwo] * 100

        bezrobocieWWojewodztwie[wojewodztwo.lower()] = "{:.2f}".format(procent) + "%"

    return bezrobocieWWojewodztwie
def przerwa():
    print('----------------------------------------')
dzialanieProgramu()
