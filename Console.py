from Domain.Obiect import to_string, get_locatie
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.Functionality import concatenare, mutare_obiect_locatie, pret_max_locatie, ordonare_crescator_pret, \
    suma_pret_locatie


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("a. Afisare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    print("u. Undo")
    print("x. Iesire")


def ui_adauga_obiect(lista, undo_list):
    try:
        ID = input("Dati ID-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret_achizitie = float(input("Dati pretul: "))
        locatie = input("Dati locatia:")
        rezultat = adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista
def ui_sterge_obiect(lista, undo_list):
    try:
        ID = input("Dati ID-ul obiectului care trebuie sters: ")
        rezultat = sterge_obiect(ID, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_modifica_obiect(lista, undo_list):
    try:
        ID = input("Dati ID-ul obiectului care trebuie modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret_achizitie = input("Dati noul pret: ")
        locatie = input("Dati noua locatie:")
        rezultat = modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))


def ui_mutare_obiect_locatie(lista, undo_list):
    ID=input("Dati ID ul: ")
    locatie = input("Dati locatia: ")
    undo_list.append(lista)
    return mutare_obiect_locatie(lista, ID, locatie)


def ui_concatenare(lista, undo_list):
    try:
        string = input("Dati stringul: ")
        pret = float(input("Dati pretul: "))
        rezultat = concatenare(lista, string, pret)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare! ", ve)


def ui_pret_max_locatie(lista):
    locatie_curenta = ""
    for obiect in sorted(lista, key=lambda rez: get_locatie(rez)):
        if get_locatie(obiect)!=locatie_curenta:
            print(get_locatie(obiect)," ",pret_max_locatie(lista,get_locatie(obiect)))
            locatie_curenta=get_locatie(obiect)


def ui_ordonare_crescator_pret(lista, undo_list):
    undo_list.append(lista)
    return ordonare_crescator_pret(lista)
def ui_suma_pret_locatie(lista):
    """
    functia afiseaza suma preturilor pentru fiecare locatie din lista
    :param lista: lista de obiecte
    """
    nume_curent = ""
    for obiect in sorted(lista, key=lambda rez: get_locatie(rez)):
        nume = get_locatie(obiect)
        if nume != nume_curent:
            print("{}: {}".format(nume, suma_pret_locatie(lista,nume)))
        nume_curent = nume


def run_menu(lista):
    undo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista, undo_list)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista, undo_list)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista, undo_list)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "4":
            lista = ui_mutare_obiect_locatie(lista, undo_list)
        elif optiune == "5":
            lista = ui_concatenare(lista, undo_list)
        elif optiune == "6":
            ui_pret_max_locatie(lista)
        elif optiune == "7":
            lista = ui_ordonare_crescator_pret(lista, undo_list)
        elif optiune == "8":
            ui_suma_pret_locatie(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                lista = undo_list.pop()
            else:
                print("Nu se poate face Undo")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")