plik = open("instrukcje.txt", "r")
odczyt = plik.readlines()
kod = []

for wers in odczyt:
    wers = wers.strip()
    wers = wers.split(' ')
    kod.append(wers)
print(kod)

def zad1():
    napis = []
    for instrukcja in kod:
        if instrukcja[0] == "DOPISZ":
            napis.append(instrukcja[1])
        if instrukcja[0] == "ZMIEN":
            napis.pop()
            napis.append(instrukcja[1])
        if instrukcja[0] == "USUN":
            napis.pop()
        if instrukcja[0] == "PRZESUN":
            if instrukcja[1] == "Z":
                napis[napis.index(instrukcja[1])] = "A"
            else:
                ascii = ord(instrukcja[1]) + 1
                zmieniony = chr(ascii)
                napis[napis.index(instrukcja[1])] = zmieniony
    print(f"zadanie 1: {len(napis)}")
    calosc = ""
    for i in napis:
        calosc += i
    print(f"zadanie 4: {calosc}")
zad1()

def zad2():
    print(kod)
    ciag = 1
    max_ciag = 0
    instrukcja = ""

    for i in range(0, 2000-1):
        if kod[i][0] == kod[i+1][0]:
            ciag += 1
            if(ciag>max_ciag):
                max_ciag = ciag
                instrukcja = kod[i][0]
        if kod[i][0] != kod[i+1][0]:
            ciag = 1
    print(f"zadanie 2: {max_ciag}, {instrukcja}")


zad2()
import statistics
def zad3():
    literki = []
    for instrukcja in kod:
        if instrukcja[0] == "DOPISZ":
            literki.append(instrukcja[1])
    print("zadanie : ")
    print(statistics.mode(literki))
    print(literki.count("Z"))





zad3()