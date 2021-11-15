def creeaza_obiect(ID, nume, descriere , pret_achizitie, locatie):
    """
    functia creeaza o lista care reprezinta un obiect
    :param ID: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: o lista care contine un obiect
    """
    #return {"ID":ID, "nume":nume, "descriere":descriere, "pret_achizitie":pret_achizitie, "locatie":locatie}
    return [ID, nume, descriere, pret_achizitie, locatie]


def get_ID(obiect):
    """
    functia da ID-ul unui obiect
    :param obiect: o lista ce contine un obiect
    :return: ID-ul obiectului
    """
    return obiect[0]


def get_nume(obiect):
    """
    functia da numele unui obiect
    :param obiect: lista ce contine un obiect
    :return: numele obbiectului
    """
    return obiect[1]


def get_descriere(obiect):
    """
    functia da clasa unui obiect
    :param obiect: lista ce contine un obiect
    :return: descrierea obiectului
    """
    return obiect[2]


def get_pret_achizitie(obiect):
    """
    functia da prteul unui obiect
    :param obiect: lista ce contine un obiect
    :return: pretul obiectului
    """
    return obiect[3]


def get_locatie(obiect):
    """
    functia da locatia unui obiect
    :param obiect: lista ce contine un obiect
    :return: locatia obiectului
    """
    return obiect[4]


def to_string(obiect):
    return "ID: {}, nume: {}, descriere: {}, pret_achizitie: {}, locatie: {}".format(
        get_ID(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret_achizitie(obiect),
        get_locatie(obiect)
    )