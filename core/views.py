from django.shortcuts import render

def index (request):
    comentario ={"titulo":"COMENTARIO ENVIADO DESDE DJANGO A LA PAGINA"}
    return render(request, "core/index.html", comentario)

def contactanos (request):
     return render(request, "core/contactanos.html")

def login (request):
     return render(request, "core/login.html")

def registro (request):

    return render(request, "core/registro.html")     




