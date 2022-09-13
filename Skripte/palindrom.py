tekst = input("Unesi tekst koji zelis da proveris da li je palindrom:\n")
print()
tekst_cap = tekst.upper()
#print(tekst_cap)
tekst_cap = tekst_cap.replace(" ", "")
#print(tekst_cap)
tekst_list = []
for slovo in tekst_cap:
    tekst_list.append(slovo)
#print(tekst_list)
list_tekst = []
for slovo in tekst_cap:
    list_tekst.insert(0,slovo)
#print(list_tekst)
bl = tekst_list == list_tekst
print(bl)



    