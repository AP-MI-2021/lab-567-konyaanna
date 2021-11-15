from Domain.Obiect import get_ID, get_pret_achizitie, get_locatie


def mutare_obiect_locatie(lista, ID, locatie):
    """
    functia are ca efect mutarea tuturor obiectelor dintr-o locatie in alta
    :param lista: lista de obiecte
    :param ID: id-ul pe care este obiectul
    :return: lista de obiecte mutate corespunzator
    """
    for obiect in lista:
        if get_ID(obiect) == ID:
            obiect[4]=locatie
    return lista


def concatenare(lista, string, pret):
    """
    functia are ca efect concatenarea unui string citit la toate descrierile obiectelor cu pretul mai mare decat o valoare citita
    :param lista: lista de obiecte
    :param string: string-ul care se va concatena la descriere
    :param pret: pretul citit
    :return: lista de obiecte modificata corespunzator
    """
    for obiect in lista:
       if get_pret_achizitie(obiect)>pret:
           obiect[2]=obiect[2]+string
    return lista


def pret_max_locatie(lista, locatie):
    """
    functia determina prețul maxim pentru o locatie.
    :param lista: lista de obiecte
    :param locatie: string
    :return: prețul maxim pentru locatia data.
    """
    for obiect in sorted(lista, key=lambda rez: get_pret_achizitie(rez), reverse=True):
        if get_locatie(obiect) == locatie:
            return get_pret_achizitie(obiect)
    return None


def ordonare_crescator_pret(lista):
    """
    functia ordoneaza obiectele din lista crescator dupa pret
    :param lista: lista de obiecte
    :return: lista ordonata crescator dupa pretul obiectelor
    """
    return sorted(lista, key=lambda rez: get_pret_achizitie(rez))


def suma_pret_locatie(lista, locatie):
    """
    functia calculeaza suma preturilor obiectelor facute pe o locatie data
    :param lista: lista de obiecte
    :param locatie: string
    :return: suma preturilor obiectelor facute pe o locatie
    """
    suma = 0
    for obiect in lista:
        if get_locatie(obiect) == locatie:
            suma = suma + get_pret_achizitie(obiect)
    return suma
