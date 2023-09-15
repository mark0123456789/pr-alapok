#feladat002
"""
kérjünk be a billentyűzetről két egész számot és
írassuk ki a két szám öszegét a képernyőre
"""
szam_1 =input("kérek egyszámot: ")
szam_1 = int(szam_1)
szam_3 = float(szam_1)
szam_2 = int(input("kérek egymásik számot:"))
Összeg = szam_1+szam_2
print(f"A megadott két szám öszege : {szam_1+szam_2}")
print(f"a megadott két szám öszege: {Összeg}")
print(f"A szam_1 változó tipusa : {type(szam_1)}")
print(f"A szam_2 változó tipusa : {type(szam_2)}")
print(f"A szam_3 változó értéke: {szam_3}")
print(f"A szam_3 változó típusa:{type(szam_3)}")
