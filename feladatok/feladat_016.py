#feladat_016
#while ciklus III.

from operator import truediv


folytatja = True
while folytatja:
    print(f"vidd ki a szemetet!")
    valasz = input('mondjam még egyszer (i/n): ')
    if valasz == 'n':
        folytatja = False
print(f"a program vége")