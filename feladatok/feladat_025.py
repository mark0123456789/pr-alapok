 
"""Üres lista és üres változó deklarálása
A megadott szavakat fűzi a listához mindaddig, amíg a felhasználó csak egy ENTER-t nem nyom, azaz nem ad meg újabb értéket."""

# üres listát hoz létre
gyumolcsok = []

# kezdőérték nélküli változót hoz létre
gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
    # hozzáfűzi a listahoz
        gyumolcsok.append(gyumolcs)

print(gyumolcsok)  
print(f"A gyümölcsök listájának száma {len(gyumolcsok)}")
