f = open("liczby.txt", "r")
ftwo = open("pierwsze.txt", "r")
odczyt = f.readlines()
odczytdwa = ftwo.readlines()


def isPrime(x):
    if x == 2:
        return True
    if x <= 1:
        return False
    if x % 2 == 0:
        return False
    for i in range(3, x):
        if x % i == 0:
            return False
    return True


def zad1():
    print("Zadanie 4.1: ")
    odp = []
    #print(isPrime(163))
    for line in odczyt:
        line = line.strip()
        if isPrime(int(line)) and int(line) >= 100 and int(line) <= 5000:
            odp.append(line)
    print(odp)
zad1()

def zad2():
    odp = []
    for line in odczytdwa:
        line = line.strip()
        if isPrime(int(line)) and isPrime(int(line[::-1])):
            odp.append(line)

    print(odp)
zad2()

def policz_wage(slowo):
    waga = 0
    for i in range(0, len(slowo)):
        waga += int(slowo[i])
    return waga

def zad3():
    odp = []

    for line in odczytdwa:
        line = line.strip()

        aktualna_waga = policz_wage(line)

        if aktualna_waga == 1:
            odp.append(line)
        else:
            while int(aktualna_waga) >= 10:
                aktualna_waga = policz_wage(str(aktualna_waga))

                if int(aktualna_waga) == 1:
                    odp.append(line)

    print(odp)






zad3()
