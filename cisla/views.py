from django.shortcuts import render

def index(request):
    sucet = 10+5
    apar="cislo a je parne"
    return render(request, 'kalkulacka/index.html',{"sucet":sucet,"apar":apar})
