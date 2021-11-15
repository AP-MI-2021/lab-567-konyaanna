from Domain.Obiect import creeaza_obiect, get_ID, get_nume, get_descriere, get_pret_achizitie, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "carte", "verde", 100, "cluj")
    assert get_ID(obiect) == "1"
    assert get_nume(obiect) == "carte"
    assert get_descriere(obiect) == "verde"
    assert get_pret_achizitie(obiect) == 100
    assert get_locatie(obiect) == "cluj"