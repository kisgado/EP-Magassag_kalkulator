import math


def magassag(tavolsag: float, alpha: float, beta: float) -> float:
    """
    Kiszámítja a tárgy magasságát.\n
    :param tavolsag: méter. ilyen messze van a tárgy a mérés helyszínétől
    :param alpha: a tárgy teteje: szög, tizedes tört formában.
    :param beta: a tárgy alja: szög, tizedes tört formában.
    :return: float, a tárgy magassága
    """

    alpha = alpha * (math.pi / 180)  # Fokból radiánba váltás
    fenti_magassag = math.tan(alpha) * tavolsag
    beta = beta * (math.pi / 180)  # Fokból radiánba váltás
    lenti_magassag = math.tan(beta) * tavolsag
    h = fenti_magassag + lenti_magassag
    return h
