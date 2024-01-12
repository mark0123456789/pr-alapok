#2023.12.01
#piringermark
#8.as
import random

randomszam = random.randint(0,1)
fej = 1
Írás = 0
print(randomszam)
válasz = input("fej vagy írás (1 ha fej 0 ha írás) ?")
if fej == randomszam and válasz:
    print("eltaláltad!")
elif fej != randomszam and válasz:
    print("nem talált")
elif Írás == randomszam and válasz:
    print("talált")
elif Írás != randomszam and válasz:
    print("nem talált")