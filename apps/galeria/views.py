from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado")
        return redirect('/login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)      #itens do banco de dados
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)      ##PK= CHAVE PRIMARIA
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não está logado")
        return redirect('/login')
    #buscando objetos do banco de dados
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)


    return render(request, 'galeria/buscar.html', {"cards" : fotografias})

def nova_imagem(request):
    return render(request, 'galeria/nova_imagem.html')

def editar_imagem(request):
    pass

def excluir_imagem(request):
    pass