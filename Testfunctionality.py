from Domain.Obiect import get_locatie, get_descriere, get_ID, get_pret_achizitie
from Logic.CRUD import adauga_obiect
from Logic.Functionality import mutare_obiect_locatie, concatenare, pret_max_locatie, suma_pret_locatie, \
    ordonare_crescator_pret


def test_mutare_obiect_locatie():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "latop", "hp", 80, "alba", lista)
    lista = adauga_obiect("3", "tabla", "alba", 110, "arad", lista)
    mutare_obiect_locatie(lista, "1","alba")
    mutare_obiect_locatie(lista, "2", "cluj")

    assert get_locatie(lista[0]) == "alba"
    assert get_locatie(lista[1]) == "cluj"
    assert get_locatie(lista[2]) == "arad"


def test_concatenare():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 101, "cluj", lista)
    lista = adauga_obiect("2", "latop", "hp", 80, "alba", lista)
    lista = adauga_obiect("3", "tabla", "alba", 110, "arad", lista)
    concatenare(lista, "abc", 100)

    assert get_descriere(lista[0]) == "verdeabc"
    assert get_descriere(lista[1]) == "hp"
    assert get_descriere(lista[2]) == "albaabc"


def test_pret_max_locatie():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "laptop", "hp", 80, "cluj", lista)
    lista = adauga_obiect("3", "tabla", "alba", 80, "alba", lista)
    lista = adauga_obiect("4", "birou", "lemn", 85, "alba", lista)
    lista = adauga_obiect("5", "catalog", "10pag", 200, "arad", lista)

    assert pret_max_locatie(lista, "cluj") == 100
    assert pret_max_locatie(lista, "alba") == 85
    assert pret_max_locatie(lista, "arad") == 200


def test_ordonare_crescator_pret():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "laptop", "hp", 80, "cluj", lista)
    lista = adauga_obiect("3", "tabla", "alba", 85, "alba", lista)
    lista=ordonare_crescator_pret(lista)

    assert get_ID(lista[0]) == "2"
    assert get_ID(lista[1]) == "3"
    assert get_ID(lista[2]) == "1"

    assert get_pret_achizitie(lista[0]) == 80
    assert get_pret_achizitie(lista[1]) == 85
    assert get_pret_achizitie(lista[2]) == 100


def test_suma_pret_locatie():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "laptop", "hp", 80, "cluj", lista)
    lista = adauga_obiect("3", "tabla", "alba", 80, "alba", lista)
    lista = adauga_obiect("4", "birou", "lemn", 85, "alba", lista)
    lista = adauga_obiect("5", "catalog", "10pag", 200, "arad", lista)

    assert suma_pret_locatie(lista, "cluj") == 180
    assert suma_pret_locatie(lista, "alba") == 165
    assert suma_pret_locatie(lista, "arad") == 200



