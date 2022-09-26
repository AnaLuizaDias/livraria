from django.http import HttpResponse

def teste(request):
    return HttpResponse("ola mundo do django")

def teste2(request):
    return HttpResponse("uma nova pagina")