from Domain.Obiect import get_ID
from Logic.CRUD import adauga_obiect


def operatii(undo_list, redo_list, lista):
    undo_list.append(lista)
    redo_list.clear()


def test_ui_undo_redo():
    undo_list = []
    redo_list = []

    lista = []

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("2", "laptop", "hp", 150, "alba", lista)
    assert len(lista) == 2

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("3", "tabla", "alba", 200, "arad", lista)
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
        assert get_ID(lista[1]) == "2"

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    assert get_ID(lista[0]) == "1"

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 0

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("2", "laptop", "hp", 150, "alba", lista)
    assert len(lista) == 2

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("3", "tabla", "alba", 200, "arad", lista)
    assert len(lista) == 3

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adauga_obiect("4", "masa", "lemn", 220, "gorj", lista)
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 1
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    assert get_ID(lista[0]) == "1"
    assert get_ID(lista[1]) == "4"

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
