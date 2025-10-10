
def cislo_na_text(cislo):
    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři",
        "pět", "šest", "sedm", "osm", "devět"
    ]
    mezi = [
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
        "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
    ]
    desitky = [
        "", "", "dvacet", "třicet", "čtyřicet",
        "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    cislo = int(cislo)

    if cislo < 0 or cislo > 100:
        return "Nemám v seznamu"
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return mezi[cislo - 10]
    elif cislo == 100:
        return "sto"
    elif cislo % 10 == 0:
        return desitky[cislo // 10]
    else:
        return f"{desitky[cislo // 10]} {jednotky[cislo % 10]}"


cislo = input("Zadej číslo od 0 do 100: ")
text = cislo_na_text(cislo)
print(text)
