# Program koji ucitava tekst i reci iz njega prebacuje u listu. Nakon toga reci sortira prema pocetnom slovu.

izbor=input("Da li zelis da uneses tekst - opcija 1 ili da ucitas fajl koji treba sortirati - opcija 2: ")

if izbor == "1":
    tekst = input("Unesi tekst koji zelis da sortiras:\n")
    print()

if izbor == "2":
    naziv_fajla=input("Unesi naziv fajla koji teba sortirati:\n")
    print()
#    txt_file = open(naziv_fajla)
#    tekst = txt_file.read()
 #   txt_file.close()
    with open(naziv_fajla, 'r') as txt_file:
        tekst = txt_file.read()
    txt_file.closed      

def cap_word(tekst):
    split_tekst = tekst.split()
    new_text = []
    for word in split_tekst:
        new_text.append(word.title())
    return new_text 
    

def list_sort(lista):
    temp = 0
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if ord(lista[i][0]) > ord(lista[j][0]):
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    return lista

sortirana_lista = list_sort(cap_word(tekst))

print("Ovo je sortiran tekst po abecednom redu: \n")
print (sortirana_lista)
















