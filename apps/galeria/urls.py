from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem, editar_imagem, excluir_imagem
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),    ##FOTO_ID VAI SER UMA VARIAVEL PARA IDENTIFICAR A FOTO
    path("buscar", buscar, name='buscar'),
    path("nova-imagem", nova_imagem, name='nova_imagem'),
    path("editar-imagem", editar_imagem, name='editar_imagem'),
    path("excluir-imagem", excluir_imagem, name='excluir_imagem'),
]

