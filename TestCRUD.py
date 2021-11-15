from Domain.Obiect import get_ID, get_nume, get_descriere, get_pret_achizitie, get_locatie
from Logic.CRUD import adauga_obiect, get_by_ID, sterge_obiect, modifica_obiect


def test_adauga_obiect():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "laptop", "hp", 110, "alba", lista)

    assert len(lista) == 2
    assert get_ID(lista[0]) == "1"
    assert get_nume(lista[0]) == "carte"
    assert get_descriere(lista[1]) == "hp"
    assert get_pret_achizitie(get_by_ID("1", lista)) == 100
    assert get_locatie(get_by_ID("2", lista)) == "alba"


def test_sterge_obiect():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "laptop", "hp", 110, "alba", lista)

    lista = sterge_obiect("1", lista)

    assert len(lista) == 1
    assert get_by_ID("1", lista) is None
    assert get_by_ID("2", lista) is not None


def test_modifica_obiect():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "laptop", "hp", 110, "alba", lista)

    lista = modifica_obiect("1", "carte", "roz", 35, "arad", lista)

    assert get_descriere(lista[0]) == "roz"
    assert get_pret_achizitie(lista[0]) == 35
    assert get_locatie(lista[0]) == "arad"
