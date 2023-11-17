szam = int(input(f'kérek egy páros számot: '))
szam_fele = int(szam/2)

darab_karakter = 1
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1    
darab_karakter = szam_fele
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor + 1    