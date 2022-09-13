text = "Marko Trnavac je car"

print(text.split())


word_count = {}
brojac = 0
for word in text.split():
    brojac += 1
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print(f'Ukupno ima:', brojac, 'reci')
print (word_count)

