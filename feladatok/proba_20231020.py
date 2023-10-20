def koszont():
    print('üdv a fedérzeten')

koszont()
koszont()
koszont()

#---------------------------------------------------------

def koszont_nevvel(nev):
    print("szia "+ nev +", üdv a fedérzeten")

koszont_nevvel('ádám')

#---------------------------------------------------------

def koszont_nevvel(nev1,nev2):
    #print("szia "+ nev1 + " , " + nev2 + "!\n üdv a fedérzeten!")
    print(f"szia {nev1}, {nev2}!\nüdva a fedérzeten! ")

keresztnev1 = "nóra"
keresztnev2 = "ádám"
koszont_nevvel("nóra",'ádám')
koszont_nevvel(keresztnev1,keresztnev2)
#--------------------------------------------------------

