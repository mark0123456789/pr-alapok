#Piringer Márk 9/c
jegy =  int(input(f"kérek egy jegyet 1 és 5 között."))
if jegy == 5:
    print(f"a jegyed {jegy}-ös ami jeles")
elif jegy == 4 :
    print(f"a jegyed {jegy}-es ami jó")
elif jegy == 3:
    print(f"a jeyged {jegy}-as ami közepes")
elif jegy == 2:
    print(f"a jeyged {jegy}-es ami elégséges")
elif jegy == 1:
    print(f"a jeyged {jegy}-es ami elégtelen")
else:
    print(f"a számod {jegy} ,ami nem megfelelő")