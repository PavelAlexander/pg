def je_tah_mozny(figura: str, start: tuple[int, int], cil: tuple[int, int], obsazene: set[tuple[int, int]]) -> bool:
    """Zjistí, zda je tah možné provést podle pravidel šachu."""

    # 1. hranice šachovnice
    if not (1 <= cil[0] <= 8 and 1 <= cil[1] <= 8):
        return False

    # 2. cílové pole nesmí být obsazené
    if cil in obsazene:
        return False

    r1, c1 = start
    r2, c2 = cil
    dr, dc = r2 - r1, c2 - c1

    # 3. pravidla pro jednotlivé figury
    if figura == "pěšec":
        # řádky rostou
        if c1 == c2:
            if r1 == 2 and dr == 2 and (r1+1, c1) not in obsazene:
                return True
            if dr == 1:
                return True
        return False

    elif figura == "jezdec":
        return (abs(dr), abs(dc)) in [(2, 1), (1, 2)]

    elif figura == "věž":
        if r1 == r2 or c1 == c2:
            if r1 == r2:  # horizontální tah
                step = 1 if c2 > c1 else -1
                for c in range(c1+step, c2, step):
                    if (r1, c) in obsazene:
                        return False
            else:  # vertikální tah
                step = 1 if r2 > r1 else -1
                for r in range(r1+step, r2, step):
                    if (r, c1) in obsazene:
                        return False
            return True
        return False

    elif figura == "střelec":
        if abs(dr) == abs(dc):
            step_r = 1 if dr > 0 else -1
            step_c = 1 if dc > 0 else -1
            r, c = r1 + step_r, c1 + step_c
            while (r, c) != (r2, c2):
                if (r, c) in obsazene:
                    return False
                r += step_r
                c += step_c
            return True
        return False

    elif figura == "dáma":
        # kombinuje věž + střelec
        return je_tah_mozny("věž", start, cil, obsazene) or je_tah_mozny("střelec", start, cil, obsazene)

    elif figura == "král":
        return abs(dr) <= 1 and abs(dc) <= 1

    return False

