#feladat_005
# dk9 104-oldal
"""
amikor karakterláncá alakítunk, az str utasításra van szükség.
"""
felhasználó_kora = 16
print(f"A felhasználó_kora változó tipusa : {type(felhasználó_kora)}")
felhasználó_kora = str(felhasználó_kora)
print(f"a felfasználó_kora változó típusa: {type(felhasználó_kora)}")
ilyen = input("És milyen" + felhasználó_kora + 'évesnek lenni?')
olyan = input(f"és milyen {felhasználó_kora} évesnek lenni?")