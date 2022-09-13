from django.shortcuts import render

# Create your views here.

def palindrom(request):
    return render(request, 'palindrom/palindrom.html')

def palout(request):
    
    tekst = request.GET.get('recenica')

    tekst_cap = tekst.upper()
    tekst_cap = tekst_cap.replace(" ", "")
    tekst_list = []
    for slovo in tekst_cap:
        tekst_list.append(slovo)
    list_tekst = []
    for slovo in tekst_cap:
        list_tekst.insert(0,slovo)
    bb = tekst_list == list_tekst
   
    
    return render(request, 'palindrom/palout.html', {'recenica':bb})