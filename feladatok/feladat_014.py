#feladat_014
"""
kérjünk be a vezeték és keresznevünket.
Írassuk ki eljárás sgítségével nevünket.
pl:
be:"kérem a vezetékneved : takács"
be:"kérem a keresztneved : istván"
ki:"a nevem: takács istván"
"""
def telyes_nev():
    vezetek=input("kérem a vezetékneved: ")
    kereszt=input("kérem a keresztneved: ")
    print(f"A nevem: {vezetek} {kereszt}")

telyes_nev()
