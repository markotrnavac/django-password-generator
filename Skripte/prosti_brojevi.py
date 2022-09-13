def delioci(broj):
    brojevi = []
    for i in range(2, broj+1):
        while broj % i == 0:
          broj = broj/i
          brojevi.append(i)
    return(brojevi)

#Unosi broj sa tastature        
uneti_broj = int(input('Unesi bilo koji pozitivan ceo broj: '))
niz_delilaca = delioci(uneti_broj)
print("Prosti brojevi, delioci unetog broja su:", niz_delilaca)