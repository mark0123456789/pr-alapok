#feladat_014
"""
kérjünk be a vezeték és keresznevünket.
Írassuk ki eljárás sgítségével nevünket.
pl:
be:"kérem a vezetékneved : takács"
be:"kérem a keresztneved : istván"
ki:"a nevem: takács istván"
"""

    vezetek=input("kérem a vezetékneved: ")
    kereszt=input("kérem a keresztneved: ")
def telyes_nev(vnev,knev):
    print(f"A nevem: {vnev} {knev}")

telyes_nev(vezetek,kereszt)
