from django.shortcuts import render

# Create your views here.

def wordcount(request):
    return render(request, 'wordcount/wordcount.html')

def wordcountout(request):
    
    tekst = request.GET.get('tekst')

    tekst.split()
    
    word_count = {}
    brojac = 0
    for word in tekst.split():
        brojac += 1
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    izlazni_tekst1 = 'Ukupno ima: ' + str(brojac) + ' reci'
       
    return render(request, 'wordcount/wordcountout.html', {'recenica1':izlazni_tekst1, 'recenica2':word_count})
