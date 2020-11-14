# Zadanie z 1 zajec

import random


def licz(x):
    list = []
    list2 = []
    for i in range(0, x):
        j = random.randint(1,50)
        if j%2==0:
            print(f"liczba {j} jest podzielna przez 2")
            list.append(j)
        else:
            print(f"liczba {j} nie jest podzielna przez 2")
            list2.append(j)
    return list, list2


try:
    value=int(input("Podaj ilosc powtorzen (od 10 do 50):"))
except ValueError:
    print("To nie jest liczba")
lista_parzystych, lista_nieparzystych = licz(value)

print(lista_parzystych)
print(lista_nieparzystych)
