import random

lista = ["abracadabra", "bomboane", "rubrica", "versiune", "amiabil"]


def alegere_cuvant_din_lista() -> list:
    """

    :return: se alege aleatoriu un cuvant din lista
    """
    cuvant_ales = random.choice(lista).upper()
    return list(cuvant_ales)


def ascunderea_literelor(orice_cuvant: list) -> list:
    """

    :param orice_cuvant: se ia ca input orice cuvant sub forma de string
    :return: se returneaza o lista cu toate literele ascunse ale cuvantului ales aleatoriu, mai putin prima si ultima.
    Daca prima sau ultima se regaseste in cuvantul ascuns, se va afisa si pozitia acestora
    din interiorul cuvantului ascuns.
    """
    lista_cuvant_ascuns = []

    # Ascundem toate literele din cuvantul ales random:
    for litera in orice_cuvant:
        lista_cuvant_ascuns.append("-")

    # Aratam prima si ultima litera a cuvantului:
    for j in lista_cuvant_ascuns:
        lista_cuvant_ascuns[0] = orice_cuvant[0]
        lista_cuvant_ascuns[len(lista_cuvant_ascuns) - 1] = orice_cuvant[len(orice_cuvant) - 1]

    # Daca prima sau ultima litera se regaseste in cuvant, aratam pozitiile in care acestea se afla:
    for t in range(len(orice_cuvant)):
        litera_1 = orice_cuvant[t]
        if litera_1 == lista_cuvant_ascuns[len(orice_cuvant) - 1]:
            lista_cuvant_ascuns[t] = orice_cuvant[t]
        if litera_1 == lista_cuvant_ascuns[0]:
            lista_cuvant_ascuns[t] = orice_cuvant[t]
    return lista_cuvant_ascuns


def stadiul_jocului():
    # Aratam stadiul jocului, literele ghicite si numarul de incercari ramase:
    print(f'Mai aveti {total_incercari - incercari} incercari:')
    print(f"Cuvantul este: {' '.join(cuvant_ascuns)}")


cuvant = alegere_cuvant_din_lista()
print(cuvant)
cuvant_ascuns = ascunderea_literelor(cuvant)
print(cuvant_ascuns)
incercari = 0
total_incercari = 7

# Crearea unui loop care sa determine daca jucatorul a castigat sau nu:

joc_terminat = False

while not joc_terminat:
    # Prezentam cate incercari disponibile mai are jucatorul si aratam cuvantul ascuns:
    stadiul_jocului()

    # Ii cerem jucatorului sa introduca o litera:
    litera_ghicita = input(f"Va rog sa introduceti o litera: ").upper()

    # Verificam daca inputul introdus de la tastatura se afla in alfabet:
    if litera_ghicita in "abcdefghijklmnopqrstuvwxyz".upper() and len(litera_ghicita) == 1:

        # Daca litera ghicita se afla deja in cuvant, informam jucatorul:
        if litera_ghicita in cuvant_ascuns:
            print(f"Litera {litera_ghicita} a mai fost folosita!")
            print("\n")

        # Daca jucatorul a ghicit litera corecta, aratam toate literele ghicite corect:
        elif litera_ghicita in cuvant:
            print(f"Litera {litera_ghicita} este corecta!")
            print("\n")
            for i in range(len(cuvant)):
                litera = cuvant[i]
                if litera == litera_ghicita:
                    cuvant_ascuns[i] = cuvant[i]
                    cuvant[i] = "-"

        # Informam jucatorul daca nu a ghicit litera corecta si
        # incrementam numarul de incercari:
        else:
            print(f"Litera {litera_ghicita} este incorecta")
            print("\n")
            incercari += 1

        # Daca jucatorul a castigat, il informam si inchidem loop-ul:
        # The all() method returns True when all elements in the given iterable are true. If not, it returns False.
        if all("-" != char for char in cuvant_ascuns):
            print("Felicitari, ati castigat!")
            print("\n")
            joc_terminat = True

        # Daca jucatorul a pierdut, il informam si inchidem loop-ul:
        if incercari >= total_incercari:
            print("Ati pierdut!")
            print("\n")
            joc_terminat = True

    # Daca jucatorul vrea sa fie funky, ii spunem sa termine cu prostiile:
    else:
        print("Nu fiti pufi si introduceti o litera, nu o hieroglifa.")
        print("\n")


