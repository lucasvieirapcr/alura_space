from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome",)      #MECANISMO DE BUSCA
    list_filter = ("categoria","usuario")    #colocando como tupla
    list_editable = ("publicada",)   #isso é para editar algo sem precisar entrar nele
    list_per_page = 10               #quero 10 itens por página

admin.site.register(Fotografia, ListandoFotografias) #Desse modo, registrei o banco de dados no Admin.
