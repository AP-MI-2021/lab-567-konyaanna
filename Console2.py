from copy import deepcopy

from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.Functionality import mutare_obiect_locatie, concatenare, ordonare_crescator_pret
from UI.Console import show_all, ui_pret_max_locatie, ui_suma_pret_locatie


def print_menu2():
    print(" add. Adaugare obiect")
    print(" delete . Stergere obiect")
    print(" modify . Modificare obiect")
    print("show . Afisare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    print("undo . Undo")
    print("redo: Redo")
    print("x. Iesire")


def ui_adauga_obiect_2(ID, nume, descriere, pret_achizitie, locatie, lista, undo_list, redo_list):
    try:
        rezultat = adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_sterge_obiect_2(ID, lista, undo_list, redo_list):
    try:
        rezultat = sterge_obiect(ID, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_modifica_obiect_2(ID, nume, descriere, pret_achizitie, locatie, lista, undo_list, redo_list):
    try:
        rezultat = modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_mutare_obiect_locatie_2(ID, locatie, lista, undo_list, redo_list):
    undo_list.append(deepcopy(lista))
    redo_list.clear()
    return mutare_obiect_locatie(lista, ID, locatie)


def ui_concatenare_2(string,pret,lista, undo_list, redo_list):
    try:
        undo_list.append(deepcopy(lista))
        rezultat = concatenare(lista, string, pret)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare! ", ve)


def ui_ordonare_crescator_pret_2(lista, undo_list, redo_list):
    undo_list.append(deepcopy(lista))
    redo_list.clear()
    return ordonare_crescator_pret(lista)


def run_menu_2(lista):
    undo_list = []
    redo_list = []
    while True:
        cerinta = input("Dati cerinta: ")
        if cerinta == "stop":
            break
        else:
            lista_cerinte = cerinta.split(";")
            for c in lista_cerinte:
                if c == "help":
                    print_menu2()
                elif c[0:3] == "add":
                    ID = c.split(",")[1]
                    nume = c.split(",")[2]
                    descriere = c.split(",")[3]
                    pret_achizitie = float(c.split(",")[4])
                    locatie = c.split(",")[5]
                    lista = ui_adauga_obiect_2(ID, nume, descriere, pret_achizitie, locatie, lista, undo_list, redo_list)
                elif c[0:4] == "show":
                    show_all(lista)
                elif c[0:6] == "delete":
                    ID = c.split(",")[1]
                    lista = ui_sterge_obiect_2(ID, lista, undo_list, redo_list)
                elif c[0:6] == "modify":
                    ID = c.split(",")[1]
                    nume = c.split(",")[2]
                    descriere = c.split(",")[3]
                    pret_achizitie = float(c.split(",")[4])
                    locatie = c.split(",")[5]
                    lista = ui_modifica_obiect_2(ID, nume, descriere, pret_achizitie, locatie, lista, undo_list, redo_list)
                elif c[0]=="4":
                    ID = c.split(",")[1]
                    locatie = c.split(",")[2]
                    ui_mutare_obiect_locatie_2(ID, locatie, lista, undo_list, redo_list)
                elif c[0]=="5":
                    string = c.split(",")[1]
                    pret = float(c.split(",")[2])
                    ui_concatenare_2(string, pret, lista, undo_list, redo_list)
                elif c[0]=="6":
                    ui_pret_max_locatie(lista)
                elif c[0]=="7":
                    lista=ui_ordonare_crescator_pret_2(lista, undo_list, redo_list)
                elif c[0]=="8":
                    ui_suma_pret_locatie(lista)
                elif c[0:4] == "undo":
                    if len(undo_list) > 0:
                        redo_list.append(lista)
                        lista = undo_list.pop()
                    else:
                        print("Nu se poate face Undo")
                elif c[0:4] == "redo":
                    if len(redo_list) > 0:
                        undo_list.append(deepcopy(lista))
                        lista = redo_list.pop()
                else:
                    print("Cerinta inexistenta! Mai incercati")