from Domain.Obiect import creeaza_obiect, get_ID


def adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lista):
    """
    functia adauga un obiect intr-o lista
    :param ID: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand atat elementele vechi cat si noul obiect
    """
    if get_by_ID(ID, lista) is not None:
        raise ValueError("ID-ul exista deja!")
    if descriere == "":
        raise ValueError("Descrierea nu poate fi nula!")
    if len(locatie) !=4:
        raise ValueError("Locatia trebuie sa aiba exact 4 caractere!")
    obiect = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)
    return lista + [obiect]


def get_by_ID(ID, lista):
    """
    functia da obiectul cu ID-ul dat dintr-o lista
    :param ID: string
    :param lista: o lista de obiecte
    :return: obiectul cu ID-ul dat din lista sau None, daca acesta nu exista
    """
    for obiect in lista:
        if get_ID(obiect) == ID:
            return obiect
    return None


def sterge_obiect(ID, lista):
    """
    functia sterge un obiect cu un ID dat din lista
    :param ID: string
    :param lista: o lista de obiecte
    :return: lista de obiecte fara obiectul cu ID-ul dat
    """
    if get_by_ID(ID, lista) is None:
        raise ValueError("Nu exista obiect cu ID-ul dat!")
    return [obiect for obiect in lista if get_ID(obiect) != ID]


def modifica_obiect(ID, nume, descriere, pret_acizitie, locatie, lista):
    """
    functia modifica o prajitura dupa ID
    :param ID: string
    :param nume: string
    :param descriere: string
    :param pret_locatie: float
    :param locatie: string
    :param lista: o lista de obiecte
    :return: lista de obiecte in care s-a modificat obiectul cu ID-ul dorit
    """
    if get_by_ID(ID, lista) is None:
        raise ValueError("Nu exista obiect cu ID-ul dat!")
    lista_noua = []
    for obiect in lista:
        if get_ID(obiect) == ID:
            obiect_nou = creeaza_obiect(ID, nume, descriere, pret_acizitie, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua