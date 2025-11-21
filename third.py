def je_prvocislo(n: int) -> bool:
    """Vrátí True pokud n je prvočíslo, jinak False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # kontrola dělení od 3 do odmocniny n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def vrat_prvocisla(maximum: int) -> list[int]:
    """Vrátí seznam všech prvočísel od 2 do maximum (včetně)."""
    return [i for i in range(2, maximum + 1) if je_prvocislo(i)]
