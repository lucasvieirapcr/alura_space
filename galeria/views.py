from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)      #itens do banco de dados
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)      ##PK= CHAVE PRIMARIA
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})


def buscar(request):
    #buscando objetos do banco de dados
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)


    return render(request, 'galeria/buscar.html', {"cards" : fotografias})