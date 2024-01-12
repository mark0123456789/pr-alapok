from operator import index


nyelvek = ['Python', 'C', 'C++', 'Java']



#keresés
keresett_elem = 'C'
if keresett_elem  in nyelvek:
    print(nyelvek.index( keresett_elem ))
else :
    print(f"nincsa listában a keresett elem : { keresett_elem }")

szamlalo = 0 
for elem in nyelvek:
    if  elem == 'Python':
        szamlalo =+ 1
    print(f"a python elelm {szamlalo} ennyiszer jelen meg ")

#bővítés 

#törlés

