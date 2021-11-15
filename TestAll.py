from Tests.TestCRUD import test_adauga_obiect, test_sterge_obiect, test_modifica_obiect
from Tests.TestDomain import test_obiect
from Tests.Testfunctionality import test_mutare_obiect_locatie, test_concatenare, test_pret_max_locatie, \
    test_ordonare_crescator_pret, test_suma_pret_locatie


def runalltests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    test_modifica_obiect()
    test_mutare_obiect_locatie()
    test_concatenare()
    test_pret_max_locatie()
    test_ordonare_crescator_pret()
    test_suma_pret_locatie()
