f=open("liczby.txt", "r")
odczyt = f.readlines()

def czy_pierwsza(x):
    if x % 2 == 0:
        return False
    for n in range(3, x):
        if x % n == 0:
            return False

    return True

odp = 0
print("Zadanie 4.1: ")
for line in odczyt:
    line = line.strip()
    if int(line[::-1]) % 17 == 0:
        odp +=1
        print(line[::-1])
#print(odp)

print("Zadanie 4.2: ")
wartosc_max = 0
linia = ""
kod = []
for line in odczyt:
    line = line.strip()
    wartosc = abs(int(line) - int(line[::-1]))
    kod.append(wartosc)
    if wartosc > wartosc_max:
        wartosc_max = wartosc
        linia = str(line)
print(wartosc_max, linia)

print("Zadanie 4.3: ")


for line in odczyt:
    line = line.strip()
    if czy_pierwsza(int(line)) and czy_pierwsza(int(line[::-1])):
        print(line)

print("Zadanie 4.4 pdpkt 1: ")

tabela = []
for line in odczyt:
    line = line.strip()
    tabela.append(line)
unikalna_tabela = set(tabela)
print(len(unikalna_tabela))

print("Zadanie 4.4 pdpkt 2: ")
powtarza_dwa = []
for y in unikalna_tabela:
    if tabela.count(y) == 2:
        powtarza_dwa.append(y)
print(len(powtarza_dwa))


print("Zadanie 4.4 pdpkt 3: ")

powtarza_trzy = []
for p in unikalna_tabela:
    if tabela.count(p) == 3:
        powtarza_trzy.append(p)

print(len(powtarza_trzy))

